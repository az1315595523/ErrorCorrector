import ast
import random
from typing import List, Dict, Any
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class ArgMutator(BaseMutator):
    def __init__(self):
        super().__init__()
        self.mutation_targets = []

    def get_mutate_types(self) -> List[str]:
        return ['RemoveArg', 'RemoveKwarg']

    def init(self):
        super().init()
        self.mutation_targets = []

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return code

        class MutationCollector(ast.NodeVisitor):
            def __init__(self, outer):
                self.outer = outer
                super().__init__()

            def visit_Call(self, node):
                for idx in range(len(node.args)):
                    self.outer.mutation_targets.append({
                        'type': 'arg',
                        'node': node,
                        'index': idx,
                        'lineno': getattr(node, 'lineno', 0)
                    })
                for idx in range(len(node.keywords)):
                    self.outer.mutation_targets.append({
                        'type': 'kwarg',
                        'node': node,
                        'index': idx,
                        'lineno': getattr(node, 'lineno', 0)
                    })
                self.generic_visit(node)

        MutationCollector(self).visit(tree)

        if not self.mutation_targets:
            return code

        target = random.choice(self.mutation_targets)

        class MutationApplier(ast.NodeTransformer):
            def __init__(self, outer, target):
                self.outer = outer
                self.target = target
                super().__init__()

            def visit_Call(self, node):

                if node == self.target['node']:
                    if self.target['type'] == 'arg':

                        removed_arg = node.args[self.target['index']]
                        original_code = ast.unparse(node)
                        node.args.pop(self.target['index'])
                        self._record_mutation(original_code, node, removed_arg, 'arg')
                    else:
                        removed_kwarg = node.keywords[self.target['index']]
                        original_code = ast.unparse(node)
                        node.keywords.pop(self.target['index'])
                        self._record_mutation(original_code, node, removed_kwarg, 'kwarg')
                return node

            def _record_mutation(self, original_code, node, removed_element, mutate_type):
                self.outer.record_mutation(
                    mutator_type="ArgMutator",
                    mutate_type=f"Remove{mutate_type.title()}",
                    line_num=self.target['lineno'],
                    original_code=original_code,
                    mutated_code=ast.unparse(node),
                    description=f"Removed {mutate_type}: {ast.unparse(removed_element)}"
                )
                self.outer.successful = True

        mutated_tree = MutationApplier(self, target).visit(tree)
        return ASTParser.tree_to_code(mutated_tree)

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return False

        mutation_targets = []

        class MutationCollector(ast.NodeVisitor):
            def visit_Call(self, node):
                for idx in range(len(node.args)):
                    mutation_targets.append({'type': 'arg'})
                for idx in range(len(node.keywords)):
                    mutation_targets.append({'type': 'kwarg'})
                self.generic_visit(node)

        MutationCollector().visit(tree)

        return len(mutation_targets) > 0
