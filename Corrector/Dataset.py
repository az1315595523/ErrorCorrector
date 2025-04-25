import os
import json

import numpy as np
import torch
from torch.utils.data import Dataset
from tqdm import tqdm

from Corrector.translation.run import extract_dataflow, parser, logger, InputFeatures
from config import CONFIG


def Convert_examples_to_features(examples, tokenizer, stage=None):
    features = []

    for example_index, example in enumerate(tqdm(examples, total=len(examples))):
        code_tokens, dfg = extract_dataflow(example['buggy_code'], parser, "python")
        code_tokens = [tokenizer.tokenize('@ ' + x )[1:] if idx != 0 else tokenizer.tokenize(x) for idx, x in
                       enumerate(code_tokens)]
        ori2cur_pos = {}
        ori2cur_pos[-1] = (0, 0)
        for i in range(len(code_tokens)):
            ori2cur_pos[i] = (ori2cur_pos[i - 1][1], ori2cur_pos[i - 1][1] + len(code_tokens[i]))
        code_tokens = [y for x in code_tokens for y in x]

        # truncating
        code_tokens = code_tokens[:CONFIG.MAX_SOURCE_LENGTH - 3][:512 - 3]

        source_tokens = [tokenizer.cls_token] + code_tokens + [tokenizer.sep_token]
        source_ids = tokenizer.convert_tokens_to_ids(source_tokens)
        position_idx = [i + tokenizer.pad_token_id + 1 for i in range(len(source_tokens))]
        dfg = dfg[:CONFIG.MAX_SOURCE_LENGTH - len(source_tokens)]
        source_tokens += [x[0] for x in dfg]
        position_idx += [0 for x in dfg]
        source_ids += [tokenizer.unk_token_id for x in dfg]
        padding_length = CONFIG.MAX_SOURCE_LENGTH - len(source_ids)
        position_idx += [tokenizer.pad_token_id] * padding_length
        source_ids += [tokenizer.pad_token_id] * padding_length
        source_mask = [1] * (len(source_tokens))
        source_mask += [0] * padding_length

        # reindex
        reverse_index = {}
        for idx, x in enumerate(dfg):
            reverse_index[x[1]] = idx
        for idx, x in enumerate(dfg):
            dfg[idx] = x[:-1] + ([reverse_index[i] for i in x[-1] if i in reverse_index],)
        dfg_to_dfg = [x[-1] for x in dfg]
        dfg_to_code = [ori2cur_pos[x[1]] for x in dfg]
        length = len([tokenizer.cls_token])
        dfg_to_code = [(x[0] + length, x[1] + length) for x in dfg_to_code]

        # target
        if stage == "test":
            target_tokens = tokenizer.tokenize("None")
        else:
            target_tokens = tokenizer.tokenize(example['fixed_code'])

            if len(target_tokens)>512:
                print("tk!", example_index,example)

            target_tokens = target_tokens[:CONFIG.MAX_TARGET_LENGTH - 2]
        target_tokens = [tokenizer.cls_token] + target_tokens + [tokenizer.sep_token]
        target_ids = tokenizer.convert_tokens_to_ids(target_tokens)
        target_mask = [1] * len(target_ids)
        padding_length = CONFIG.MAX_TARGET_LENGTH - len(target_ids)
        target_ids += [tokenizer.pad_token_id] * padding_length
        target_mask += [0] * padding_length

        if example_index < 5:
            if stage == 'train':
                logger.info("*** Example ***")
                logger.info("source_tokens: {}".format([x.replace('\u0120', '_') for x in source_tokens]))
                logger.info("source_ids: {}".format(' '.join(map(str, source_ids))))
                logger.info("source_mask: {}".format(' '.join(map(str, source_mask))))
                logger.info("position_idx: {}".format(position_idx))
                logger.info("dfg_to_code: {}".format(' '.join(map(str, dfg_to_code))))
                logger.info("dfg_to_dfg: {}".format(' '.join(map(str, dfg_to_dfg))))

                logger.info("target_tokens: {}".format([x.replace('\u0120', '_') for x in target_tokens]))
                logger.info("target_ids: {}".format(' '.join(map(str, target_ids))))
                logger.info("target_mask: {}".format(' '.join(map(str, target_mask))))

        features.append(
            InputFeatures(
                example_index,
                source_ids,
                position_idx,
                dfg_to_code,
                dfg_to_dfg,
                target_ids,
                source_mask,
                target_mask,
            )
        )
    return features


def ReadData(data_dir):
    data = []
    all_files = os.listdir(data_dir)
    # print(len(all_files))
    base_files = [f for f in all_files if '_err' not in f and 'info' not in f]
    # print(len(base_files))
    # print(base_files)
    for base_file in base_files:
        base_name = base_file
        base_path = os.path.join(data_dir, base_file)

        # print(base_name, base_path)

        with open(base_path, "r", encoding="utf-8") as f:
            fixed_code = f.read()

        for err_idx in range(CONFIG.MUTATION_SIZE):
            err_file = f"{base_name}_err_{err_idx}.py"
            err_path = os.path.join(data_dir, err_file)
            # print("err_file", err_file)
            if not os.path.exists(err_path):
                continue
            with open(err_path, "r", encoding="utf-8") as f:
                buggy_code = f.read()

            mutated_info = ""
            info_file = f"{base_name}_info_{err_idx}.json"
            # print("info_file", info_file)
            info_path = os.path.join(data_dir, info_file)
            if os.path.exists(info_path):
                with open(info_path, "r", encoding="utf-8") as f:
                    info_json = json.load(f)
                    mutated_info = "\n".join(
                        [item["mutated_info"] for item in info_json.get("single_Info", [])]
                    )
            sample = {"buggy_code": buggy_code, "fixed_code": fixed_code, "mutated_info": mutated_info, "file_name":err_file}
            data.append(sample)
        print(f"Loaded {len(data)} samples from {data_dir}")
    return data


class CodeCorrectDataset(Dataset):
    def __init__(self, data):

        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        attn_mask = np.zeros((CONFIG.MAX_SOURCE_LENGTH, CONFIG.MAX_SOURCE_LENGTH), dtype=bool)

        node_index = sum([i > 1 for i in self.data[item].position_idx])
        max_length = sum([i != 1 for i in self.data[item].position_idx])

        attn_mask[:node_index, :node_index] = True

        for idx, i in enumerate(self.data[item].source_ids):
            if i in [0, 2]:
                attn_mask[idx, :max_length] = True

        for idx, (a, b) in enumerate(self.data[item].dfg_to_code):
            if a < node_index and b < node_index:
                attn_mask[idx + node_index, a:b] = True
                attn_mask[a:b, idx + node_index] = True

        for idx, nodes in enumerate(self.data[item].dfg_to_dfg):
            for a in nodes:
                if a + node_index < len(self.data[item].position_idx):
                    attn_mask[idx + node_index, a + node_index] = True
        np.fill_diagonal(attn_mask, True)

        row_sums = attn_mask.sum(axis=1)
        if (row_sums == 0).any():
            print(f"警告：样本 {item} 的 attn_mask 存在全零行！")

        return (torch.tensor(self.data[item].source_ids),
                torch.tensor(self.data[item].source_mask),
                torch.tensor(self.data[item].position_idx),
                torch.tensor(attn_mask),
                torch.tensor(self.data[item].target_ids),
                torch.tensor(self.data[item].target_mask),)
