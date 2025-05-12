import logging
import math
import os
import random

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
from mutators.ArgMutator import ArgMutator
from mutators.ArrayMutator import ArrayMutator
from mutators.ControlFlowMutator import ControlFlowMutator
from mutators.EmptyStructureMutator import EmptyStructureMutator
from torch.utils.data import DataLoader, RandomSampler
from Corrector.modelTrain import train, load_model, predict, BLEUEvaluate
from Judge.statistic import run_python_files
from Judge.statistic2 import save_statistics_report
from Judge.statistic3 import Code_Analysis

def test():
    M = ModuleMutator()
    with open('datasets/s60.py', 'r') as f:
        correct_code = f.read()

    muCode = M.mutate(correct_code)
    print(correct_code)
    print(
        "-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-")
    print(muCode)

    print("mutateInfo:", M.mutation_record)
    print(sum(CONFIG.MUTATION_RATE))

    print(sum(CONFIG.MUTATION_TIMES_RATE))


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
    model, tokenizer = load_model(CONFIG.SAVE_DIR + "/pytorch_model.bin")

    examples = []
    all_files = os.listdir('data/test_code')
    all_files = [f for f in all_files if f.endswith('.py')]
    for file in all_files:
        base_path = os.path.join('data/test_code', file)
        with open(base_path, "r", encoding="utf-8") as f:
            buggy_code = f.read()
            example = {
                'buggy_code': buggy_code,
                'fixed_code': "None"
            }
            examples.append(example)
    examples = random.choices(examples, k=10)
    feature = Convert_examples_to_features(examples, tokenizer, "test")
    device = torch.device("cuda" if torch.cuda.is_available() and not CONFIG.NO_CUDA else "cpu")
    p = predict(model, feature, tokenizer, device)
    for i in range(10):
        print("buggy_code", examples[i]['buggy_code'])
        print("fixed_code", p[i])


def test6():
    mutators = [
        QuoteMutator(),
        FunctionMutator(),
        OperatorMutator(),
        ModuleMutator(),
        VariableNameMutator(),
        EmptyStructureMutator(),
        ControlFlowMutator(),
        ConditionMutator(),
        IndentMutator(),
        ColonMutator()
    ]

    datasets_folder = 'datasets'
    if not os.path.exists(datasets_folder):
        print(f"文件夹 {datasets_folder} 不存在。")
        return
    python_files = [f for f in os.listdir(datasets_folder) if f.endswith('.py')]
    for file in python_files:
        file_path = os.path.join(datasets_folder, file)
        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            print(f"正在测试文件: {file}")
            # 对每个变异器进行测试
            for mutator in mutators:
                result = mutator.can_mutate(code)
                print(f"  {mutator.__class__.__name__}: {'可以变异' if result else '无法变异'}")
        except Exception as e:
            print(f"读取文件 {file} 时出错: {e}")

def test7():

    with open('datasets/s1.py', 'r') as f:
        original_code = f.read()

    mutators = [
        BracketMutator(),
        ColonMutator(),
        FunctionMutator(),
        IndentMutator(),
        ModuleMutator(),
        OperatorMutator(),
        QuoteMutator(),
        VariableNameMutator(),
        ConditionMutator(),
        BoundaryMutator(),
        ArrayMutator(),
        ArgMutator(),
        ControlFlowMutator(),
        EmptyStructureMutator()
    ]
    available_mutators = [m for m in mutators if m.can_mutate(original_code)]
    mutators_with_none = available_mutators + [None]
    index_list = [mutators.index(m) for m in available_mutators]
    available_rates = [CONFIG.MUTATION_RATE[i] for i in index_list]

    rates_with_none = available_rates + [1 - sum(CONFIG.MUTATION_RATE)]

    time = random.choices(range(min(len(CONFIG.MUTATION_TIMES_RATE), len(index_list))),
                          weights=CONFIG.MUTATION_TIMES_RATE[:len(available_mutators)], k=1)[0]
    mutators = random.choices(mutators_with_none, weights=rates_with_none, k=time)
    print(f"time:{time}")
    print(mutators)
    print(rates_with_none)


def test8():
    model, tokenizer = load_model(CONFIG.SAVE_DIR + "/pytorch_model.bin")
    device = torch.device("cuda" if torch.cuda.is_available() and not CONFIG.NO_CUDA else "cpu")

    BLEUEvaluate(model, tokenizer, device, CONFIG.TEST_OUTPUT)


if __name__ == '__main__':
    # run_python_files(CONFIG.OUTPUT_DIR,CONFIG.LOG_DIR)
    # save_statistics_report(CONFIG.OUTPUT_DIR, CONFIG.LOG_DIR)
    Code_Analysis(CONFIG.INPUT_DIR, CONFIG.LOG_DIR)
    # train(True)
    # test5()
    # test4()
    # test6()
    # test7()
    # print(sum(CONFIG.MUTATION_RATE))
    # test2()
    # test3()
    # test()
    # pipeline = DataPipeline()
    # pipeline.generate_dataset(
    #     input_dir=CONFIG.INPUT_DIR,
    #     output_dir=CONFIG.OUTPUT_DIR
    # )
