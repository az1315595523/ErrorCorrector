from mutators.BaseMutator import BaseMutator
import re
import random


class QuoteMutator(BaseMutator):
    def __init__(self):
        super().__init__()

    def get_mutate_types(self):
        return ['QSingle_to_double', 'QUnterminated', 'QEscape_remove']

    def mutate(self, code: str) -> str:
        lines = code.splitlines()
        for i, line in enumerate(lines):
            if '"' in line or "'" in line:
                quote_pos = max(line.find('"'), line.find("'"))
                if quote_pos == -1:
                    continue

                mutation_type = self.select_mutation_type()
                original_line = line

                mutated_line = original_line
                desc = ""

                if mutation_type == 'QSingle_to_double':
                    mutated_line = line.replace("'", '"')
                    desc = f"Changed single to double quotes at line {i + 1}"
                    self.successful = True
                elif mutation_type == 'QUnterminated':
                    mutated_line = line[:quote_pos] + line[quote_pos + 1:]
                    desc = f"Removed opening quote at line {i + 1}"
                    self.successful = True
                self.record_mutation(
                    mutator_type="QuoteMutator",
                    mutate_type=mutation_type,
                    line_num=i + 1,
                    original_code=original_line,
                    mutated_code=mutated_line,
                    description=desc
                )
                lines[i] = mutated_line
                return '\n'.join(lines)
        return code