import logging
import os

import torch
from torch import nn
from transformers import AutoTokenizer, AutoModel, RobertaConfig, RobertaModel, RobertaTokenizer

from Corrector.Dataset import CodeCorrectDataset, ReadData, Convert_examples_to_features
from Corrector.translation.model import Seq2Seq
from config import CONFIG
from dataPipeline import DataPipeline
from mutators.BracketMutator import BracketMutator
from mutators.ColonMutator import ColonMutator
from mutators.FunctionMutator import FunctionMutator
from mutators.IndentMutator import IndentMutator
from mutators.ModuleMutator import ModuleMutator
from mutators.QuoteMutator import QuoteMutator
from mutators.VariableNameMutator import VariableNameMutator
from mutators.OperatorMutator import OperatorMutator
from mutators.ConditionMutator import ConditionMutator
from mutators.BoundaryMutator import BoundaryMutator
from mutators.ArrayMutator import ArrayMutator
from torch.utils.data import DataLoader, RandomSampler
from Corrector.modelTrain import train, load_model, predict


def test():
    M = BoundaryMutator()
    with open('s-2910-001.py', 'r') as f:
        correct_code = f.read()

    muCode = M.mutate(correct_code)
    print(correct_code)
    print(
        "-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-")
    print(muCode)

    print("mutateInfo:", M.mutation_record)


def test2():
    buggy_code = """

    def add(a,b)
        return a+b

    """


def test3():
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base")

    source_code = "def add(a, b):\n return a +"

    input_ids = tokenizer("fix: " + source_code, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    fixed_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(fixed_code)


def test4():
    tokenizer = AutoTokenizer.from_pretrained(CONFIG.ENCODER_PATH)
    encoder = AutoModel.from_pretrained(CONFIG.ENCODER_PATH)

    config_class, model_class, tokenizer_class = RobertaConfig, RobertaModel, RobertaTokenizer
    config = config_class.from_pretrained(CONFIG.ENCODER_PATH)

    decoder_layer = nn.TransformerDecoderLayer(d_model=config.hidden_size, nhead=config.num_attention_heads)
    decoder = nn.TransformerDecoder(decoder_layer, num_layers=6)

    model = Seq2Seq(encoder=encoder, decoder=decoder, config=encoder.config,
                    beam_size=CONFIG.BEAM_SIZE, max_length=CONFIG.MAX_TARGET_LENGTH,
                    sos_id=tokenizer.cls_token_id, eos_id=tokenizer.sep_token_id)

    data = ReadData(CONFIG.TRAIN_DATA_DIR)
    feature_with_data = Convert_examples_to_features(data, tokenizer, "train")
    dataset = CodeCorrectDataset(feature_with_data)

    train_loader = DataLoader(
        dataset,
        batch_size=CONFIG.BATCH_SIZE // CONFIG.GRADIENT_ACCUMULATION_STEPS,
        sampler=RandomSampler(dataset),
        num_workers=4
    )

    batch = next(iter(train_loader))
    device = torch.device("cuda" if torch.cuda.is_available() and not CONFIG.NO_CUDA else "cpu")
    batch = tuple(t.to(device) for t in batch)
    model.to(device)
    model.eval()
    torch.backends.cuda.enable_flash_sdp(True)
    source_ids, source_mask, position_idx, att_mask, target_ids, target_mask = batch
    print(f"source_ids:{source_ids},source_mask:{source_mask},position_idx{position_idx},att_mask{att_mask}"
          f",target_ids{target_ids},target_mask{target_mask}")
    with torch.no_grad():
        output = model(source_ids, source_mask, position_idx, att_mask, target_ids, target_mask)
    # 输出结果
    print("前向传播结果:", output)


def test5():
    buggy_code = """

    a = float(input())
    b = int(input())
    d = a
    if b > 1:
        for d in range(-1, b):
            c = a * (1 / 2) ** d
            d = d + c * 2
        print('%.2f' % d)
    else:
        print('%.2f' % d)

    """
    model, tokenizer = load_model(CONFIG.SAVE_DIR + "/checkpoint-last/pytorch_model.bin")
    example = {
        'buggy_code': buggy_code,
        'fixed_code': "None"
    }
    examples = []
    examples.append(example)
    feature = Convert_examples_to_features(examples, tokenizer, "test")
    device = torch.device("cuda" if torch.cuda.is_available() and not CONFIG.NO_CUDA else "cpu")
    p = predict(model, feature, tokenizer, device)
    print(p)


if __name__ == '__main__':
    # train(True)
    # test4()
    test5()
# test2()
# test3()
# test()
#     pipeline = DataPipeline()
#     pipeline.generate_dataset(
#         input_dir=CONFIG.INPUT_DIR,
#         output_dir=CONFIG.OUTPUT_DIR
#     )
