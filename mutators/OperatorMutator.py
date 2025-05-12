import ast
import copy
import random

from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class OperatorMutator(BaseMutator):

    def __init__(self):
        super().__init__()
        self.mutate_type = None
        self.operator_mapping = {
            # Arithmetic
            ast.Add: [ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow],
            ast.Sub: [ast.Add, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow],
            ast.Mult: [ast.Add, ast.Sub, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow],
            ast.Div: [ast.Add, ast.Sub, ast.Mult, ast.FloorDiv, ast.Mod, ast.Pow],
            ast.FloorDiv: [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow],
            ast.Mod: [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Pow],
            ast.Pow: [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod],

            # Comparison
            ast.Eq: [ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE],
            ast.NotEq: [ast.Eq, ast.Lt, ast.LtE, ast.Gt, ast.GtE],
            ast.Lt: [ast.Eq, ast.NotEq, ast.LtE, ast.Gt, ast.GtE],
            ast.LtE: [ast.Eq, ast.NotEq, ast.Lt, ast.Gt, ast.GtE],
            ast.Gt: [ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.GtE],
            ast.GtE: [ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt],
        }
        self.find_BinOp = False
        self.find_Compare = False
        self.code_lines = []

    def get_mutate_types(self):
        return ['BinOpSubs', 'CompareSubs']

    def init(self):
        super().init()
        self.find_BinOp = False
        self.find_Compare = False
        self.code_lines = []

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return False

        class OperatorFinder(ast.NodeVisitor):
            def __init__(self):
                self.found = False

            def visit_BinOp(self, node):
                if type(node.op) in self.operator_mapping:
                    self.found = True
                self.generic_visit(node)

            def visit_Compare(self, node):
                for op in node.ops:
                    if type(op) in self.operator_mapping:
                        self.found = True
                self.generic_visit(node)

        finder = OperatorFinder()
        finder.operator_mapping = self.operator_mapping
        finder.visit(tree)
        return finder.found

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)

        outer_self = self

        self.mutate_type = self.select_mutation_type()

        class OperatorTransformer(ast.NodeTransformer):
            def visit_BinOp(self, node):
                if outer_self.mutate_type == 'BinOpSubs':
                    if type(node.op) in outer_self.operator_mapping:
                        return outer_self._mutate_operator(node)
                return node

            def visit_Compare(self, node):
                if outer_self.mutate_type == 'CompareSubs':
                    for i, op in enumerate(node.ops):
                        if type(op) in outer_self.operator_mapping:
                            return outer_self._mutate_comparison(node, i)
                return node

        mutated = OperatorTransformer().visit(tree)
        return ASTParser.tree_to_code(mutated)

    def _mutate_operator(self, node: ast.BinOp) -> ast.BinOp:
        original_code = ASTParser.tree_to_code(node)
        original_op = type(node.op).__name__
        new_op_type = random.choice(self.operator_mapping[type(node.op)])
        node.op = new_op_type()

        self.successful = True
        self.record_mutation(
            mutator_type="OperatorMutator",
            mutate_type=self.mutate_type,
            line_num=getattr(node, 'lineno', 0),
            original_code=original_code,
            mutated_code=ASTParser.tree_to_code(node),
            description=f"Replaced {original_op} with {new_op_type.__name__} in binary operation"
        )
        self._mutation_applied = True
        return node

    def _mutate_comparison(self, node: ast.Compare, op_index: int) -> ast.Compare:
        original_code = ASTParser.tree_to_code(node)
        original_op = type(node.ops[op_index]).__name__
        new_op_type = random.choice(self.operator_mapping[type(node.ops[op_index])])
        node.ops[op_index] = new_op_type()

        self.successful = True
        self.record_mutation(
            mutator_type="OperatorMutator",
            mutate_type=self.mutate_type,
            line_num=getattr(node, 'lineno', 0),
            original_code=original_code,
            mutated_code=ASTParser.tree_to_code(node),
            description=f"Replaced {original_op} with {new_op_type.__name__} in comparison"
        )
        self._mutation_applied = True
        return node
