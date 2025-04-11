import json
import random

from config import CONFIG
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
import os


class DataPipeline:
    def __init__(self):
        self.mutators = [
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
            ArrayMutator()
        ]

    def generate_dataset(self, input_dir, output_dir):
        os.makedirs(output_dir, exist_ok=True)

        for filename in os.listdir(input_dir):
            with open(os.path.join(input_dir, filename), 'r') as f:
                original_code = f.read()

            samples = []

            mutators_with_none = self.mutators + [None]
            rates_with_none = CONFIG.MUTATION_RATE + [1 - sum(CONFIG.MUTATION_RATE)]

            for i in range(10):
                print("time:", i)
                time = random.choices(range(12), weights=CONFIG.MUTATION_TIMES_RATE, k=1)[0]
                mutators = random.choices(mutators_with_none, weights=rates_with_none, k=time)
                mutated = original_code
                singleMutationInfo = []
                count = 0
                for mutator in mutators:
                    print("mutator:", type(mutator).__name__)
                    if mutator is None:
                        continue
                    try:
                        print("ori:", mutated)
                        mutated = mutator.mutate(mutated)
                        print("mutated:", mutated)
                        print("info", mutator.mutation_record)
                        print("isSuccessful:",mutator.successful)
                        count += 1
                        if mutator.successful:
                            singleMutationInfo.append({
                                'mutated_info': str(mutator.mutation_record),
                                'mutator_type': type(mutator).__name__
                            })
                            mutator.init()
                    except Exception as e:
                        print(e)
                        break
                total_Mutation_Info = {
                    'expectedTimes': time,
                    'times': len(singleMutationInfo),
                    'realTimes': count,
                    'single_Info': singleMutationInfo
                }
                samples.append({
                    'mutated_code': mutated,
                    'mutation_info': total_Mutation_Info
                })


            for i, sample in enumerate(samples):
                code_path = os.path.join(output_dir, f"{filename}_err_{i}.py")
                info_path = os.path.join(output_dir, f"{filename}_info_{i}.json")

                with open(code_path, 'w', encoding='utf-8') as f:
                    f.write(sample['mutated_code'])

                with open(info_path, 'w', encoding='utf-8') as f_info:
                    json.dump(sample['mutation_info'], f_info, indent=2, ensure_ascii=False)

