import ast
import random
from typing import Dict, List, Set
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class FunctionCollector(ast.NodeVisitor):
    def __init__(self):
        self.defined_functions: Set[str] = set()
        self.called_functions: Set[str] = set()

    def visit_FunctionDef(self, node):
        self.defined_functions.add(node.name)
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.called_functions.add(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            self.called_functions.add(node.func.attr)
        self.generic_visit(node)


class FunctionMutator(BaseMutator):
    def __init__(self):
        super().__init__()

        self.FUNCTION_REPLACEMENTS: Dict[str, List[str]] = {
            'min': ['max', 'sum','abs'],
            'max': ['min', 'abs','sum'],
            'len': ['sum'],
            'sorted': ['reversed'],
            'abs': ['round'],
        }

    def get_mutate_types(self) -> List[str]:
        return ['FunctionReplace']

    def init(self):
        super().init()

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return False

        collector = FunctionCollector()
        collector.visit(tree)

        all_callable_functions = collector.called_functions.union(collector.defined_functions)
        replaceable_funcs = [func for func in all_callable_functions if func in self.FUNCTION_REPLACEMENTS]
        return bool(replaceable_funcs)

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return code

        collector = FunctionCollector()
        collector.visit(tree)

        all_callable_functions = collector.called_functions.union(collector.defined_functions)

        replaceable_funcs = [func for func in all_callable_functions if func in self.FUNCTION_REPLACEMENTS]
        if not replaceable_funcs:
            return code

        old_func = random.choice(replaceable_funcs)
        new_func = random.choice(self.FUNCTION_REPLACEMENTS[old_func])

        outer_self = self
        class FunctionRenamer(ast.NodeTransformer):
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id == old_func:
                    original_code = f"{old_func}(...)"
                    mutated_code = f"{new_func}(...)"
                    node.func.id = new_func
                    outer_self.record_mutation(
                        mutator_type="FunctionMutator",
                        mutate_type="FunctionReplace",
                        line_num=getattr(node, 'lineno', 0),
                        original_code=original_code,
                        mutated_code=mutated_code,
                        description=f"Replaced function call {old_func}() with {new_func}()"
                    )
                    outer_self.successful = True
                return self.generic_visit(node)

        mutated_tree = FunctionRenamer().visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return ASTParser.tree_to_code(mutated_tree)
