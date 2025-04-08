from mutators.ColonMutator import ColonMutator
from mutators.BracketMutator import BracketMutator
from validator import DataValidator
import os


class DataPipeline:
    def __init__(self):
        self.mutators = [
            ColonMutator(error_rate=0.4),
            BracketMutator(error_rate=0.3)
        ]

    def generate_dataset(self, input_dir, output_dir):
        os.makedirs(output_dir, exist_ok=True)

        for filename in os.listdir(input_dir):
            with open(os.path.join(input_dir, filename), 'r') as f:
                correct_code = f.read()

            samples = []
            for _ in range(10):  # 每个样本生成10个变体
                mutated = correct_code
                for mutator in self.mutators:
                    mutated = mutator.mutate(mutated)
                samples.append({
                    'original': correct_code,
                    'err': mutated,
                    'filename': filename
                })

            # 批量验证
            valid_samples = DataValidator.batch_validate(samples)

            # 保存结果
            for i, sample in enumerate(valid_samples):
                output_path = os.path.join(output_dir,
                                           f"{filename}_err_{i}.py")
                with open(output_path, 'w') as f:
                    f.write(f"# Original: {filename}\n")
                    f.write(f"# Error Type: Syntax\n\n")
                    f.write(sample['err'])