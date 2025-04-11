import builtins
import keyword
import ast
import random
import difflib
import string

from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class VariableCollector(ast.NodeVisitor):
    def __init__(self):
        self.excluded_names = set()
        self.variables = set()
        self.function_names = set()
        self.class_names = set()
        self.builtins = set(dir(builtins))

    def visit_FunctionDef(self, node):
        self.function_names.add(node.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.class_names.add(node.name)
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.excluded_names.add(alias.name)

    def visit_Name(self, node):
        if (
                isinstance(node.ctx, (ast.Store, ast.Load))
                and not keyword.iskeyword(node.id)
                and node.id not in self.function_names
                and node.id not in self.class_names
                and node.id not in self.builtins
                and node.id not in self.excluded_names

        ):
            self.variables.add(node.id)

    
def get_renew_variable(old_var):
    chars = string.ascii_letters + string.digits
    return old_var + random.choice(chars)


def get_weighted_random_variable(old_var, candidates):
    if not candidates:
        return get_renew_variable(old_var)
    similarity_scores = [
        difflib.SequenceMatcher(None, old_var, var).ratio()
        for var in candidates
    ]
    total = sum(similarity_scores)
    if total == 0:
        similarity_scores = [1 / len(candidates)] * len(candidates)
    else:
        similarity_scores = [score / total for score in similarity_scores]

    new_var = random.choices(candidates, weights=similarity_scores, k=1)[0]
    return new_var


class VariableNameMutator(BaseMutator):
    def __init__(self):
        super().__init__()
    
    def init(self):
        super().init()
    
    def get_mutate_types(self):
        return ['VRenew', 'VReplace']
    def select_mutation_type(self):
        rate = [0.1, 0.9]
        return random.choices(self.get_mutate_types(),weights=rate,k=1)[0]

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        collector = VariableCollector()
        collector.visit(tree)
        variables = list(collector.variables)
        if not variables:
            return code

        old_var = random.choice(variables)
        mutate_type = self.select_mutation_type()

        if mutate_type == 'renew':
            new_var = get_renew_variable(old_var)
        else:
            candidates = [v for v in variables if v != old_var]
            new_var = get_weighted_random_variable(old_var, candidates)

        outer_self = self

        class VariableRenamer(ast.NodeTransformer):
            def visit_Name(inner_self, node):
                if node.id == old_var:
                    self.successful = True
                    outer_self.record_mutation(
                        mutator_type="VariableNameMutator",
                        mutate_type=mutate_type,
                        line_num=getattr(node, 'lineno', 0),
                        original_code=node.id,
                        mutated_code=new_var,
                        description=f"Renamed '{old_var}' to '{new_var}'"
                    )
                    return ast.copy_location(ast.Name(id=new_var, ctx=node.ctx), node)
                return node

        tree = VariableRenamer().visit(tree)
        return ASTParser.tree_to_code(tree)
