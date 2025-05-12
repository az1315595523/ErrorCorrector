import ast
import random
from _ast import BoolOp, AST

from ASTParser import  ASTParser
from mutators.OperatorMutator import OperatorMutator  # 导入已有的操作符变异器


class ConditionMutator(OperatorMutator):
    def __init__(self):
        super().__init__()
        self.condition_nodes = []
        self.mutate_types = [
            'CompareSubs',  # From CompareMutator
            'LogicOpReverse',
            'ConditionNegate',
            'BoundaryAdjust',
            'PartialCondition'
        ]

    def get_mutate_types(self):
        return self.mutate_types

    def init(self):
        super().init()
        self.condition_nodes = []

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return False

        self.condition_nodes = []
        self._collect_conditions(tree)

        if not self.condition_nodes:
            return False

        for node in self.condition_nodes:
            test_node = node.test
            if isinstance(test_node, ast.Compare):
                for op in test_node.ops:
                    if type(op) in self.operator_mapping:
                        return True
            elif isinstance(test_node, ast.BoolOp):
                return True

        return False

    def mutate(self, code: str) -> str:
        self.code_lines = code.split('\n')
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return code

        self._collect_conditions(tree)
        if not self.condition_nodes:
            return code

        target_node = random.choice(self.condition_nodes)
        self.mutate_type = self.select_mutation_type()

        outer_self = self

        class ConditionTransformer(ast.NodeTransformer):
            def visit_If(self, node):
                return self._process_condition(node, node.test)

            def visit_While(self, node):
                return self._process_condition(node, node.test)

            def _process_condition(self, node, test_node):
                if node == target_node:
                    original_code = ASTParser.tree_to_code(test_node)
                    if not isinstance(test_node, ast.Compare):
                        mutate_types = [m for m in outer_self.mutate_types if m != 'CompareSubs']
                    else:
                        mutate_types = outer_self.mutate_types
                    random.shuffle(mutate_types)
                    for mutate_type in mutate_types:
                        outer_self.mutate_type = mutate_type
                        if mutate_type == 'CompareSubs':
                            new_test = outer_self._mutate_compare_op(test_node)
                        else:
                            new_test = outer_self._apply_custom_mutation(test_node, outer_self.mutate_type)
                        if outer_self.successful:
                            break

                    mutated_code = ASTParser.tree_to_code(new_test)

                    outer_self.record_mutation(
                        mutator_type="ConditionMutator",
                        mutate_type=outer_self.mutate_type,
                        line_num=getattr(node, 'lineno', 0),
                        original_code=original_code,
                        mutated_code=mutated_code,
                        description=f"{outer_self.mutate_type}: {original_code} → {mutated_code}"
                    )
                    outer_self.successful = True
                    node.test = new_test
                return node

        mutated_tree = ConditionTransformer().visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return ASTParser.tree_to_code(mutated_tree)

    def _collect_conditions(self, node):

        class ConditionCollector(ast.NodeVisitor):
            def visit_If(self, node):
                outer.condition_nodes.append(node)
                self.generic_visit(node)

            def visit_While(self, node):
                outer.condition_nodes.append(node)
                self.generic_visit(node)

        outer = self
        ConditionCollector().visit(node)

    def _mutate_compare_op(self, test_node: ast.AST):
        if isinstance(test_node, ast.Compare):
            for i in range(len(test_node.ops)):
                if type(test_node.ops[i]) in self.operator_mapping:
                    return super()._mutate_comparison(test_node, i)
        return test_node

    def _apply_custom_mutation(self, node: ast.AST, mutation_type: str) -> ast.AST:
        if mutation_type == 'LogicOpReverse':
            return self._reverse_logic_operator(node)
        elif mutation_type == 'ConditionNegate':
            return ast.UnaryOp(op=ast.Not(), operand=node)
        elif mutation_type == 'BoundaryAdjust':
            return self._adjust_boundary(node)
        elif mutation_type == 'PartialCondition':
            return self._simplify_condition(node)
        return node

    def _reverse_logic_operator(self, node: ast.AST) -> BoolOp | AST:
        if isinstance(node, ast.BoolOp):
            self.successful = True
            return ast.BoolOp(
                op=ast.Or() if isinstance(node.op, ast.And) else ast.And(),
                values=node.values
            )
        return node

    def _adjust_boundary(self, node: ast.AST) -> ast.AST:
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            self.successful = True
            op_map = {
                ast.Lt: ast.LtE,
                ast.LtE: ast.Lt,
                ast.Gt: ast.GtE,
                ast.GtE: ast.Gt
            }
            if type(node.ops[0]) in op_map:
                node.ops[0] = op_map[type(node.ops[0])]()
        return node

    def _simplify_condition(self, node: ast.AST) -> ast.AST:
        if isinstance(node, ast.BoolOp):
            self.successful = True
            return random.choice(node.values)
        return node