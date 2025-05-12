import copy
import os
import random

import logging
import numpy as np
import torch
from torch.optim import AdamW
from torch.utils.data import random_split, RandomSampler, DataLoader, SequentialSampler
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoModel, EncoderDecoderModel, AutoConfig, \
    AutoModelForCausalLM, GPT2LMHeadModel, AutoModelForSeq2SeqLM, TrainingArguments, Trainer, \
    get_linear_schedule_with_warmup
import torch.nn as nn

from Corrector.translation.bleu import _bleu
from config import CONFIG
from Corrector.Dataset import CodeCorrectDataset, ReadData, Convert_examples_to_features
from Corrector.translation.model import Seq2Seq
from Corrector.translation.bleu import compute_bleu

def train(do_eval=False):
    logger = logging.getLogger(__name__)

    # model
    tokenizer = AutoTokenizer.from_pretrained(CONFIG.ENCODER_PATH)
    encoder = AutoModel.from_pretrained(CONFIG.ENCODER_PATH)
    decoder_layer = nn.TransformerDecoderLayer(d_model=encoder.config.hidden_size,
                                               nhead=encoder.config.num_attention_heads)
    decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)
    model = Seq2Seq(encoder=encoder, decoder=decoder, config=encoder.config,
                    beam_size=CONFIG.BEAM_SIZE, max_length=CONFIG.MAX_TARGET_LENGTH,
                    sos_id=tokenizer.cls_token_id, eos_id=tokenizer.sep_token_id)

    device = torch.device("cuda" if torch.cuda.is_available() and not CONFIG.NO_CUDA else "cpu")
    model.to(device)
    # dataset
    data = ReadData(CONFIG.TRAIN_DATA_DIR)
    train_size = int(0.9 * len(data))
    eval_size = len(data) - train_size

    train_data, eval_data = random_split(data, [train_size, eval_size])
    eval_sample = [data[i] for i in eval_data.indices]
    feature_with_data = Convert_examples_to_features(train_data, tokenizer, "train")
    train_dataset = CodeCorrectDataset(feature_with_data)
    train_loader = DataLoader(
        train_dataset,
        batch_size=CONFIG.BATCH_SIZE // CONFIG.GRADIENT_ACCUMULATION_STEPS,
        sampler=RandomSampler(train_dataset),
        num_workers=4
    )
    # train_parameter
    no_decay = ['bias', 'LayerNorm.weight']
    optimizer_grouped_parameters = [
        {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
         'weight_decay': CONFIG.WEIGHT_DECAY},
        {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
    ]
    optimizer = AdamW(optimizer_grouped_parameters, lr=CONFIG.LEARNING_RATE, eps=CONFIG.ADAM_EPSILON)
    scheduler = get_linear_schedule_with_warmup(optimizer,
                                                num_warmup_steps=len(train_loader) * CONFIG.EPOCHS * 0.1,
                                                num_training_steps=len(train_loader) * CONFIG.EPOCHS)

    # Start training
    logger.info("***** Running training *****")
    logger.info("  Num examples = %d", len(train_dataset))
    logger.info("  Batch size = %d", CONFIG.BATCH_SIZE)
    logger.info("  Num epoch = %d", CONFIG.EPOCHS)

    model.train()
    dev_dataset = {}
    nb_tr_examples, nb_tr_steps, tr_loss, global_step, best_bleu, best_loss = 0, 0, 0, 0, 0, 1e6
    for epoch in range(CONFIG.EPOCHS):
        bar = tqdm(train_loader, total=len(train_loader))
        for batch in bar:
            batch = tuple(t.to(device) for t in batch)
            # print(batch)
            source_ids, source_mask, position_idx, att_mask, target_ids, target_mask = batch
            # print(f"source_ids:{source_ids},source_mask:{source_mask},position_idx{position_idx},att_mask{att_mask}"
            #       f",target_ids{target_ids},target_mask{target_mask}")
            loss, _, _ = model(source_ids, source_mask, position_idx, att_mask, target_ids, target_mask)

            if CONFIG.GRADIENT_ACCUMULATION_STEPS > 1:
                loss = loss / CONFIG.GRADIENT_ACCUMULATION_STEPS

            tr_loss += loss.item()
            train_loss = round(tr_loss * CONFIG.GRADIENT_ACCUMULATION_STEPS / (nb_tr_steps + 1), 4)
            # print(f"tr_loss:{tr_loss},loss:{loss.item()},train_loss:{train_loss}")
            bar.set_description("epoch {} loss {}".format(epoch, train_loss))
            nb_tr_examples += source_ids.size(0)
            nb_tr_steps += 1
            loss.backward()

            if (nb_tr_steps + 1) % CONFIG.GRADIENT_ACCUMULATION_STEPS == 0:
                # Update parameters
                optimizer.step()
                optimizer.zero_grad()
                scheduler.step()
                global_step += 1
        if do_eval and epoch in [int(CONFIG.EPOCHS * (i + 1) // 5) for i in range(5)]:
            # Eval model with dev dataset
            tr_loss = 0
            nb_tr_examples, nb_tr_steps = 0, 0
            if 'dev_loss' in dev_dataset:
                eval_samples, eval_data_set = dev_dataset['dev_loss']
            else:
                eval_samples = copy.deepcopy(eval_sample)
                eval_features = Convert_examples_to_features(eval_samples, tokenizer, stage='dev')
                eval_data_set = CodeCorrectDataset(eval_features)
                dev_dataset['dev_loss'] = eval_samples, eval_data_set
            logger.info("\n***** Running evaluation *****")
            logger.info("  Num examples = %d", len(eval_samples))
            logger.info("  Batch size = %d", CONFIG.BATCH_SIZE)

            eval_sampler = SequentialSampler(eval_data_set)
            eval_dataloader = DataLoader(eval_data_set, sampler=eval_sampler, batch_size=CONFIG.BATCH_SIZE,
                                         num_workers=4)
            # Start Evaling model
            model.eval()
            eval_loss, tokens_num = 0, 0
            for batch in eval_dataloader:
                batch = tuple(t.to(device) for t in batch)
                source_ids, source_mask, position_idx, att_mask, target_ids, target_mask = batch
                with torch.no_grad():
                    _, loss, num = model(source_ids, source_mask, position_idx, att_mask, target_ids, target_mask)
                eval_loss += loss.sum().item()
                tokens_num += num.sum().item()
            # Pring loss of dev dataset
            model.train()
            eval_loss = eval_loss / tokens_num
            result = {'eval_ppl': round(np.exp(eval_loss), 5),
                      'global_step': global_step + 1,
                      'train_loss': round(train_loss, 5)}
            for key in sorted(result.keys()):
                logger.info("  %s = %s", key, str(result[key]))
            logger.info("  " + "*" * 20)

            # save last checkpoint
            last_output_dir = os.path.join(CONFIG.SAVE_DIR, 'checkpoint-last')
            if not os.path.exists(last_output_dir):
                os.makedirs(last_output_dir)
            model_to_save = model.module if hasattr(model, 'module') else model  # Only save the model it-self
            output_model_file = os.path.join(last_output_dir, "pytorch_model.bin")
            torch.save(model_to_save.state_dict(), output_model_file)
            if eval_loss < best_loss:
                logger.info("  Best ppl:%s", round(np.exp(eval_loss), 5))
                logger.info("  " + "*" * 20)
                best_loss = eval_loss
                # Save best checkpoint for best ppl
                output_dir = os.path.join(CONFIG.SAVE_DIR, 'checkpoint-best-ppl')
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                model_to_save = model.module if hasattr(model, 'module') else model  # Only save the model it-self
                output_model_file = os.path.join(output_dir, "pytorch_model.bin")
                torch.save(model_to_save.state_dict(), output_model_file)

            if 'dev_bleu' in dev_dataset:
                eval_samples, eval_data_set = dev_dataset['dev_bleu']
            else:
                eval_samples = copy.deepcopy(eval_sample)
                print(type(eval_sample), type(eval_samples))
                print("random", random, type(random))
                eval_samples = random.sample(eval_samples, min(100, len(eval_samples)))
                eval_features = Convert_examples_to_features(eval_samples, tokenizer, stage='test')
                eval_data_set = CodeCorrectDataset(eval_features)
                dev_dataset['dev_bleu'] = eval_samples, eval_data_set

            eval_sampler = SequentialSampler(eval_data_set)
            eval_dataloader = DataLoader(eval_data_set, sampler=eval_sampler, batch_size=CONFIG.BATCH_SIZE,
                                         num_workers=4)
            model.eval()
            p = []
            for batch in eval_dataloader:
                batch = tuple(t.to(device) for t in batch)
                source_ids, source_mask, position_idx, att_mask, target_ids, target_mask = batch
                with torch.no_grad():
                    preds = model(source_ids, source_mask, position_idx, att_mask)
                    for pred in preds:
                        t = pred[0].cpu().numpy()
                        t = list(t)
                        if 0 in t:
                            t = t[:t.index(0)]
                        text = tokenizer.decode(t, clean_up_tokenization_spaces=False)
                        p.append(text)
            model.train()
            predictions = []
            accs = []
            with open(os.path.join(CONFIG.SAVE_DIR, "dev.output"), 'w') as f, open(
                    os.path.join(CONFIG.SAVE_DIR, "dev.gold"), 'w') as f1:
                for ref, gold in zip(p, eval_samples):
                    predictions.append(ref)
                    f.write(ref + '\n')
                    f1.write(gold['fixed_code'] + '\n')
                    accs.append(ref == gold['fixed_code'])
            dev_bleu = round(
                _bleu(os.path.join(CONFIG.SAVE_DIR, "dev.gold"), os.path.join(CONFIG.SAVE_DIR, "dev.output")), 2)
            xmatch = round(np.mean(accs) * 100, 4)
            logger.info("  %s = %s " % ("bleu-4", str(dev_bleu)))
            logger.info("  %s = %s " % ("xMatch", str(round(np.mean(accs) * 100, 4))))
            logger.info("  " + "*" * 20)

            if dev_bleu + xmatch > best_bleu:
                logger.info("  Best BLEU+xMatch:%s", dev_bleu + xmatch)
                logger.info("  " + "*" * 20)
                best_bleu = dev_bleu + xmatch
                # Save best checkpoint for best bleu
                output_dir = os.path.join(CONFIG.SAVE_DIR, 'checkpoint-best-bleu')
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                model_to_save = model.module if hasattr(model, 'module') else model  # Only save the model it-self
                output_model_file = os.path.join(output_dir, "pytorch_model.bin")
                torch.save(model_to_save.state_dict(), output_model_file)


def load_model(checkpoint_path):
    tokenizer = AutoTokenizer.from_pretrained(CONFIG.ENCODER_PATH)
    encoder = AutoModel.from_pretrained(CONFIG.ENCODER_PATH)
    decoder_layer = torch.nn.TransformerDecoderLayer(
        d_model=encoder.config.hidden_size,
        nhead=encoder.config.num_attention_heads
    )
    decoder = torch.nn.TransformerDecoder(decoder_layer, num_layers=6)
    model = Seq2Seq(
        encoder=encoder,
        decoder=decoder,
        config=encoder.config,
        beam_size=CONFIG.BEAM_SIZE,
        max_length=CONFIG.MAX_TARGET_LENGTH,
        sos_id=tokenizer.cls_token_id,
        eos_id=tokenizer.sep_token_id
    )
    model.load_state_dict(torch.load(checkpoint_path))
    return model, tokenizer


def predict(model, features, tokenizer, device):
    dataset = CodeCorrectDataset(features)
    dataloader = DataLoader(
        dataset,
        batch_size=1,
        sampler=SequentialSampler(dataset),
    )
    print(device)
    model.to(device)
    model.eval()
    predictions = []
    bar = tqdm(dataloader, total=len(dataloader))
    for batch in bar:
        batch = tuple(t.to(device) for t in batch)
        source_ids, source_mask, position_idx, att_mask, _, _ = batch

        with torch.no_grad():
            preds = model(source_ids, source_mask, position_idx, att_mask)

        for pred in preds:
            t = pred[0].cpu().numpy()
            t = list(t)
            if 0 in t:
                t = t[:t.index(0)]
            text = tokenizer.decode(t, skip_special_tokens=True)
            predictions.append(text)
    return predictions


def BLEUEvaluate(model, tokenizer, device, data_path):
    dev_dataset = {}
    eval_sample = ReadData(data_path)
    logger = logging.getLogger(__name__)
    if 'dev_bleu' in dev_dataset:
        eval_samples, eval_data_set = dev_dataset['dev_bleu']
    else:
        eval_samples = copy.deepcopy(eval_sample)
        print(type(eval_sample), type(eval_samples))
        print("random", random, type(random))
        eval_samples = random.sample(eval_samples, min(100, len(eval_samples)))
        eval_features = Convert_examples_to_features(eval_samples, tokenizer, stage='test')
        eval_data_set = CodeCorrectDataset(eval_features)
        dev_dataset['dev_bleu'] = eval_samples, eval_data_set

    eval_sampler = SequentialSampler(eval_data_set)
    eval_dataloader = DataLoader(eval_data_set, sampler=eval_sampler, batch_size=CONFIG.BATCH_SIZE,
                                 num_workers=4)
    model.eval()
    p = []
    for batch in eval_dataloader:
        batch = tuple(t.to(device) for t in batch)
        source_ids, source_mask, position_idx, att_mask, target_ids, target_mask = batch
        with torch.no_grad():
            preds = model(source_ids, source_mask, position_idx, att_mask)
            for pred in preds:
                t = pred[0].cpu().numpy()
                t = list(t)
                if 0 in t:
                    t = t[:t.index(0)]
                text = tokenizer.decode(t, clean_up_tokenization_spaces=False)
                p.append(text)
    model.train()
    predictions = []
    accs = []
    with open(os.path.join(CONFIG.SAVE_DIR, "dev.output"), 'w') as f, open(
            os.path.join(CONFIG.SAVE_DIR, "dev.gold"), 'w') as f1:
        for ref, gold in zip(p, eval_samples):
            predictions.append(ref)
            f.write(ref + '\n')
            f1.write(gold['fixed_code'] + '\n')
            accs.append(ref == gold['fixed_code'])
    dev_bleu = round(
        _bleu(os.path.join(CONFIG.SAVE_DIR, "dev.gold"), os.path.join(CONFIG.SAVE_DIR, "dev.output")), 2)
    xmatch = round(np.mean(accs) * 100, 4)
    logger.info("  %s = %s " % ("bleu-4", str(dev_bleu)))
    logger.info("  %s = %s " % ("xMatch", str(xmatch)))
    logger.info("  " + "*" * 20)
