from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator
import random


class BracketMutator(BaseMutator):
    def __init__(self):
        super().__init__()
        self.BRACKET_PAIRS = {'(': ')', '[': ']', '{': '}'}
        self._mutation_applied = False

    def get_mutate_types(self):
        return ['BDelete_start', 'BDelete_end', 'BAdd_extra', 'BReplace']

    def init(self):
        super().init()
        self._mutation_applied = False

    def mutate(self, code: str) -> str:
        lines = code.splitlines()
        bracket_pairs = self._find_all_bracket_pairs(code)
        if not bracket_pairs:
            return code

        start_pos, end_pos, start_line, end_line = random.choice(bracket_pairs)
        mutation_type = self.select_mutation_type()

        original_start_line = lines[start_line]
        original_end_line = lines[end_line] if start_line != end_line else original_start_line

        if mutation_type == 'BDelete_start':
            lines[start_line] = original_start_line[:start_pos] + original_start_line[start_pos + 1:]
            desc = f"Deleted opening bracket at line {start_line + 1}"
        elif mutation_type == 'BDelete_end':
            lines[end_line] = original_end_line[:end_pos] + original_end_line[end_pos + 1:]
            desc = f"Deleted closing bracket at line {end_line + 1}"
        elif mutation_type == 'BAdd_extra':
            new_bracket = random.choice(list(self.BRACKET_PAIRS.keys()))
            lines[start_line] = original_start_line[:start_pos] + new_bracket + original_start_line[start_pos:]
            desc = f"Added extra opening {new_bracket} at line {start_line + 1}"
        elif mutation_type == 'BReplace':
            new_pair = random.choice(list(self.BRACKET_PAIRS.items()))
            lines[start_line] = original_start_line[:start_pos] + new_pair[0] + original_start_line[start_pos + 1:]
            lines[end_line] = original_end_line[:end_pos] + new_pair[1] + original_end_line[end_pos + 1:]
            desc = f"Replaced brackets with {new_pair[0]}{new_pair[1]} at lines {start_line + 1}-{end_line + 1}"


        self.record_mutation(
            mutator_type="BracketMutator",
            mutate_type=mutation_type,
            line_num=start_line + 1,
            original_code=original_start_line,
            mutated_code=lines[start_line],
            description=desc
        )
        self.successful = True

        return '\n'.join(lines)

    def _find_all_bracket_pairs(self, code: str):
        lines = code.splitlines()
        bracket_pairs = []

        for line_num, line in enumerate(lines):
            stack = []
            for pos, char in enumerate(line):
                if char in self.BRACKET_PAIRS:
                    stack.append((char, pos, line_num))
                elif char in self.BRACKET_PAIRS.values():
                    if stack and self.BRACKET_PAIRS[stack[-1][0]] == char:
                        start_char, start_pos, start_line = stack.pop()
                        bracket_pairs.append((
                            start_pos,
                            pos,
                            start_line,
                            line_num
                        ))

        return bracket_pairs