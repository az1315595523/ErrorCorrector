from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator
import ast
import random


class ColonMutator(BaseMutator):
    def __init__(self):
        super().__init__()

    def get_mutate_types(self):
        return ['CRemove', 'CReplace']

    def mutate(self, code):
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return code

        lines = code.splitlines()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.If, ast.For)):
                line_num = node.lineno - 1
                original_line = lines[line_num]
                colon_pos = original_line.find(':', node.col_offset)

                if colon_pos != -1:
                    mutation_type = self.select_mutation_type()
                    if mutation_type == 'CRemove':
                        mutated_line = original_line[:colon_pos] + original_line[colon_pos + 1:]
                        desc = f"Removed colon at line {line_num + 1}"
                        self.successful = True
                    else:
                        mutated_line = original_line[:colon_pos] + ';' + original_line[colon_pos + 1:]
                        desc = f"Replaced colon with semicolon at line {line_num + 1}"
                        self.successful = True

                    self.record_mutation(
                        mutator_type="ColonMutator",
                        mutate_type=mutation_type,
                        line_num=line_num + 1,
                        original_code=original_line,
                        mutated_code=mutated_line,
                        description=desc
                    )
                    lines[line_num] = mutated_line
                    return '\n'.join(lines)
        return code