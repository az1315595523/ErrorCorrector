import ast
import random
from typing import List, Dict
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class FlowCollector(ast.NodeVisitor):
    def __init__(self, outer):
        self.outer = outer
        super().__init__()
        self.keyword_map = {
            ast.Break: 'break',
            ast.Continue: 'continue',
            ast.Pass: 'pass'
        }

    def visit_Break(self, node):
        self._record_node(node, 'break')
        return node

    def visit_Continue(self, node):
        self._record_node(node, 'continue')
        return node

    def visit_Pass(self, node):
        self._record_node(node, 'pass')
        return node

    def _record_node(self, node, keyword_type):
        print("keyType", keyword_type)
        self.outer.mutation_targets.append({
            'node': node,
            'type': keyword_type,
            'lineno': getattr(node, 'lineno', 0)
        })


class ControlFlowMutator(BaseMutator):
    def __init__(self):
        super().__init__()

        self.FLOW_KEYWORDS = {
            'break': ['continue', 'pass'],
            'continue': ['break', 'pass'],
            'pass': ['break', 'continue']
        }
        self.mutation_targets = []

    def get_mutate_types(self) -> List[str]:
        return ['FlowKeywordSwap']

    def init(self):
        super().init()
        self.mutation_targets = []

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return False

        FlowCollector(self).visit(tree)
        res = bool(self.mutation_targets)

        self.init()

        return res

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        if not tree:
            return code

        FlowCollector(self).visit(tree)

        if not self.mutation_targets:
            return code

        target = random.choice(self.mutation_targets)

        class FlowChanger(ast.NodeTransformer):
            def __init__(self, outer, target):
                self.outer = outer
                self.target = target
                super().__init__()

            def visit_Break(self, node):
                return self._process_node(node, 'break')

            def visit_Continue(self, node):
                return self._process_node(node, 'continue')

            def visit_Pass(self, node):
                return self._process_node(node, 'pass')

            def _process_node(self, node, current_type):
                if node == self.target['node']:
                    new_keyword = random.choice(
                        self.outer.FLOW_KEYWORDS[self.target['type']]
                    )
                    self._record_mutation(node, new_keyword)
                    return ast.parse(new_keyword).body[0]
                return node

            def _record_mutation(self, original_node, new_keyword):
                self.outer.record_mutation(
                    mutator_type="ControlFlowMutator",
                    mutate_type="FlowKeywordSwap",
                    line_num=self.target['lineno'],
                    original_code=self.target['type'],
                    mutated_code=new_keyword,
                    description=f"Changed {self.target['type']} to {new_keyword}"
                )
                self.outer.successful = True

        mutated_tree = FlowChanger(self, target).visit(tree)
        return ASTParser.tree_to_code(mutated_tree)
