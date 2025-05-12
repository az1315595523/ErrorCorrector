import ast
import random
from typing import Dict, List, Set
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class ModuleCollector(ast.NodeVisitor):
    def __init__(self):
        self.imported_modules: Set[str] = set()
        self.used_modules: Dict[str, Set[str]] = {}
        self.import_nodes = []

    def visit_Import(self, node):
        self.import_nodes.append(node)
        for alias in node.names:
            module_name = alias.name.split('.')[0]
            self.imported_modules.add(module_name)
            if alias.asname:
                self.used_modules.setdefault(module_name, set()).add(alias.asname)
            else:
                self.used_modules.setdefault(module_name, set()).add(module_name.split('.')[0])
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        self.import_nodes.append(node)
        if node.module:
            module_name = node.module.split('.')[0]
            self.imported_modules.add(module_name)
            for alias in node.names:
                if alias.asname:
                    self.used_modules.setdefault(module_name, set()).add(alias.asname)
                else:
                    self.used_modules.setdefault(module_name, set()).add(alias.name)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name):
            module_name = node.value.id
            if module_name in self.imported_modules:
                self.used_modules.setdefault(module_name, set()).add(module_name)
        self.generic_visit(node)


class ModuleMutator(BaseMutator):
    def __init__(self):
        super().__init__()
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
            'logging': ['loguru', 'structlog', 'syslog'],
            'typing': ['typing_extensions', 'collections.abc'],
            'List': ['Sequence', 'MutableSequence', 'Iterable'],
            'Optional': ['Union', 'Any', 'object']
        }

    def init(self):
        super().init()

    def get_mutate_types(self) -> List[str]:
        return ['ModuleReplace', 'ModuleRemove']

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

        mutation_type = random.choice(self.get_mutate_types())
        old_module = random.choice(replaceable_modules)

        if mutation_type == 'ModuleReplace':
            return self._replace_module(tree, old_module, collector)
        else:
            return self._remove_module(tree, old_module, collector)

    def _replace_module(self, tree, old_module, collector):
        new_module = random.choice(self.MODULE_REPLACEMENTS[old_module])
        used_aliases = collector.used_modules.get(old_module, {old_module})

        class ModuleRenamer(ast.NodeTransformer):
            def visit_Import(self, node):
                for alias in node.names:
                    if alias.name.split('.')[0] == old_module:
                        original_code = ASTParser.tree_to_code(node)
                        alias.name = alias.name.replace(old_module, new_module, 1)

                        outer_self.record_mutation(
                            mutator_type="ModuleMutator",
                            mutate_type="ModuleReplace",
                            line_num=getattr(node, 'lineno', 0),
                            original_code=original_code,
                            mutated_code=ast.unparse(node),
                            description=f"Replaced {old_module} with {new_module}"
                        )
                return node

            def visit_ImportFrom(self, node):
                if node.module and node.module.split('.')[0] == old_module:
                    original_code = ASTParser.tree_to_code(node)
                    node.module = node.module.replace(old_module, new_module, 1)

                    outer_self.record_mutation(
                        mutator_type="ModuleMutator",
                        mutate_type="ModuleReplace",
                        line_num=getattr(node, 'lineno', 0),
                        original_code=original_code,
                        mutated_code=ast.unparse(node),
                        description=f"Replaced {old_module} with {new_module}"
                    )
                return node

        outer_self = self
        mutated_tree = ModuleRenamer().visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return ASTParser.tree_to_code(mutated_tree)

    def _remove_module(self, tree, module_to_remove, collector):
        class ModuleRemover(ast.NodeTransformer):
            def visit_Import(self, node):
                new_names = [alias for alias in node.names if alias.name.split('.')[0] != module_to_remove]
                if new_names != node.names:
                    outer_self.record_mutation(
                        mutator_type="ModuleMutator",
                        mutate_type="ModuleRemove",
                        line_num=getattr(node, 'lineno', 0),
                        original_code=ast.unparse(node),
                        mutated_code=ast.unparse(ast.Import(names=new_names)) if new_names else "",
                        description=f"Removed {module_to_remove} from import"
                    )
                return ast.Import(names=new_names) if new_names else None

            def visit_ImportFrom(self, node):
                if node.module and node.module.split('.')[0] == module_to_remove:
                    outer_self.record_mutation(
                        mutator_type="ModuleMutator",
                        mutate_type="ModuleRemove",
                        line_num=getattr(node, 'lineno', 0),
                        original_code=ast.unparse(node),
                        mutated_code="",
                        description=f"Removed {module_to_remove} import"
                    )
                    return None
                return node

        outer_self = self
        mutated_tree = ModuleRemover().visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return ASTParser.tree_to_code(mutated_tree)

    def can_mutate(self, code: str) -> bool:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return False

        collector = ModuleCollector()
        collector.visit(tree)

        replaceable_modules = [
            mod for mod in collector.imported_modules
            if mod in self.MODULE_REPLACEMENTS
        ]
        return bool(replaceable_modules)