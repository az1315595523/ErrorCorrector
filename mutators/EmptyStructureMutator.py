import ast
import random
from typing import List

from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class CandidateCollector(ast.NodeVisitor):

    def __init__(self, outer, candidates):
        self.outer = outer
        self.candidates = candidates

    def visit_Assign(self, node):
        if isinstance(node.value, (ast.List, ast.Dict, ast.Call)):
            ori_type = type(node.value)
            if ori_type in self.outer.STRUCTURE_MAP:
                if ori_type == ast.Call:
                    if isinstance(node.value.func, ast.Name) and node.value.func.id == 'set' and not node.value.args:
                        self.candidates.append((node, ori_type))
                elif ori_type == ast.List or ori_type == ast.Dict:
                    self.candidates.append((node, ori_type))
        self.generic_visit(node)


class EmptyStructureMutator(BaseMutator):
    def __init__(self):
        super().__init__()
        self.STRUCTURE_MAP = {
            ast.List: [ast.Dict, ast.Call],
            ast.Dict: [ast.List, ast.Call],
            ast.Call: [ast.List, ast.Dict]
        }

    def init(self):
        super().init()

    def get_mutate_types(self) -> List[str]:
        return ['EmptyInitSwap']

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return False

        candidates = []

        CandidateCollector(self, candidates).visit(tree)
        return bool(candidates)

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return code

        candidates = []

        CandidateCollector(self, candidates).visit(tree)

        if not candidates:
            return code
        print(candidates)
        target_node, original_type = random.choice(candidates)
        original_node_code = ASTParser.tree_to_code(target_node)
        new_type = random.choice(self.STRUCTURE_MAP[original_type])

        if new_type == ast.Dict:
            target_node.value = ast.Dict(keys=[], values=[])
        elif new_type == ast.List:
            target_node.value = ast.List(elts=[])
        elif new_type == ast.Call:
            target_node.value = ast.Call(func=ast.Name(id='set', ctx=ast.Load()), args=[], keywords=[])

        self.record_mutation(
            mutator_type="EmptyStructureMutator",
            mutate_type="EmptyInitSwap",
            line_num=getattr(target_node, 'lineno', 0),
            original_code=original_node_code,
            mutated_code=ASTParser.tree_to_code(target_node),
            description=f"Changed {original_type.__name__} to {new_type.__name__}"
        )
        self.successful = True

        return ASTParser.tree_to_code(tree)
