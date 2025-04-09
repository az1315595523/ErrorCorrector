import os

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
def test():
    M = BoundaryMutator()
    with open('s-2910-001.py', 'r') as f:
        correct_code = f.read()

    muCode = M.mutate(correct_code)
    print(correct_code)
    print("-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-")
    print(muCode)

    print("mutateInfo:", M.mutation_record)


# test()

pipeline = DataPipeline()
pipeline.generate_dataset(
    input_dir=CONFIG.INPUT_DIR,
    output_dir=CONFIG.OUTPUT_DIR
)