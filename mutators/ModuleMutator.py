import ast
import random
from typing import Dict, List, Set
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class ModuleCollector(ast.NodeVisitor):
    def __init__(self):
        self.imported_modules: Set[str] = set()
        self.used_modules: Dict[str, Set[str]] = {}

    def visit_Import(self, node):
        for alias in node.names:
            module_name = alias.name.split('.')[0]
            self.imported_modules.add(module_name)
            if alias.asname:
                self.used_modules.setdefault(module_name, set()).add(alias.asname)
            else:
                self.used_modules.setdefault(module_name, set()).add(module_name.split('.')[0])

    def visit_ImportFrom(self, node):
        if node.module:
            module_name = node.module.split('.')[0]
            self.imported_modules.add(module_name)
            for alias in node.names:
                if alias.asname:
                    self.used_modules.setdefault(module_name, set()).add(alias.asname)
                else:
                    self.used_modules.setdefault(module_name, set()).add(alias.name)

    def visit_Attribute(self, node):

        if isinstance(node.value, ast.Name):
            module_name = node.value.id
            if module_name in self.imported_modules:
                self.used_modules.setdefault(module_name, set()).add(module_name)
        self.generic_visit(node)


class ModuleMutator(BaseMutator):
    def __init__(self, error_rate: float = 0.3):
        super().__init__(error_rate)

        self.MODULE_REPLACEMENTS: Dict[str, List[str]] = {
            'os': ['sys', 'pathlib', 'shutil'],
            'sys': ['os', 'platform', 'argparse'],
            'math': ['numpy', 'cmath', 'statistics'],
            'random': ['numpy.random', 'secrets'],
            'datetime': ['time', 'calendar', 'arrow'],
            'json': ['pickle', 'yaml', 'xml'],
            're': ['fnmatch', 'string', 'regex'],
            'collections': ['itertools', 'heapq', 'bisect'],
            'subprocess': ['os', 'multiprocessing', 'asyncio'],
            'logging': ['loguru', 'structlog', 'syslog']
        }

    def get_mutate_types(self) -> List[str]:
        return ['ModuleReplace']

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return code

        collector = ModuleCollector()
        collector.visit(tree)

        replaceable_modules = [
            mod for mod in collector.imported_modules
            if mod in self.MODULE_REPLACEMENTS
        ]

        if not replaceable_modules:
            return code

        old_module = random.choice(replaceable_modules)
        new_module = random.choice(self.MODULE_REPLACEMENTS[old_module])
        used_aliases = collector.used_modules.get(old_module, {old_module})

        class ModuleRenamer(ast.NodeTransformer):
            def visit_Import(self, node):
                for alias in node.names:
                    if alias.name.split('.')[0] == old_module:
                        original_name = alias.name
                        original_asname = alias.asname
                        new_name = alias.name.replace(old_module, new_module, 1)
                        alias.name = new_name
                        original_code = f"import {original_name}" + (
                            f" as {original_asname}" if original_asname else "")
                        mutated_code = f"import {new_name}" + (f" as {original_asname}" if original_asname else "")

                        outer_self.record_mutation(
                            mutator_type="ModuleMutator",
                            mutate_type="ModuleReplace",
                            line_num=getattr(node, 'lineno', 0),
                            original_code=original_code,
                            mutated_code=mutated_code,
                            description=f"Replaced module {old_module} with {new_module}"
                        )
                return node

            def visit_ImportFrom(self, node):
                if node.module and node.module.split('.')[0] == old_module:
                    original_module = node.module
                    original_names = [a.name for a in node.names]

                    new_module_base = new_module.split('.')[0]
                    node.module = node.module.replace(old_module, new_module_base, 1)

                    original_code = f"from {original_module} import {', '.join(original_names)}"
                    mutated_code = f"from {new_module_base} import {', '.join(original_names)}"
                    outer_self.record_mutation(
                        mutator_type="ModuleMutator",
                        mutate_type="ModuleReplace",
                        line_num=getattr(node, 'lineno', 0),
                        original_code=original_code,
                        mutated_code=mutated_code,
                        description=f"Replaced module {old_module} with {new_module}"
                    )
                return node

            def visit_Attribute(self, node):
                if (isinstance(node.value, ast.Name) and
                        node.value.id in used_aliases):
                    if node.value.id in used_aliases:
                        node.value.id = new_module.split('.')[0]
                return node

            def visit_Name(self, node):
                if node.id in used_aliases:
                    node.id = new_module.split('.')[0]
                return node

        outer_self = self
        mutated_tree = ModuleRenamer().visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return ASTParser.tree_to_code(mutated_tree)