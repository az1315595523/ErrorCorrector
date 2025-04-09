from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator
import random


class IndentMutator(BaseMutator):
    def __init__(self):
        super().__init__()

    def get_mutate_types(self):
        return ['IAdd_space', 'IRemove_space', 'IMix_tabs']

    def mutate(self, code) :
        lines = code.splitlines()
        for i, line in enumerate(lines):
            if line.strip() and line[0] in (' ', '\t'):
                mutation_type = self.select_mutation_type()
                original_line = line
                indent = len(line) - len(line.lstrip())
                mutated_line = original_line
                desc = ""
                if mutation_type == 'IAdd_space':
                    mutated_line = ' ' * (indent + 4) + line.lstrip()
                    desc = f"Added 4 spaces at line {i + 1}"
                    self.successful = True
                elif mutation_type == 'IRemove_space':
                    mutated_line = ' ' * max(0, indent - 4) + line.lstrip()
                    desc = f"Removed 4 spaces at line {i + 1}"
                    self.successful = True

                self.record_mutation(
                    mutator_type="IndentMutator",
                    mutate_type=mutation_type,
                    line_num=i + 1,
                    original_code=original_line,
                    mutated_code=mutated_line,
                    description=desc
                )
                lines[i] = mutated_line
                return '\n'.join(lines)
        return code
