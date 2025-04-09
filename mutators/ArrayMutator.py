import ast
import random
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class ArrayIndexCollector(ast.NodeVisitor):

    def __init__(self):
        self.index_nodes = []

    def visit_Subscript(self, node):
        if isinstance(node.slice, ast.Index) or hasattr(ast, 'Constant'):
            self.index_nodes.append(node)
        self.generic_visit(node)


class ArrayMutator(BaseMutator):
    def __init__(self):
        super().__init__()
        self.index_operations = {
            ast.Add: "-",
            ast.Sub: "+",
            None: ["+", "-"]  # 原始索引无操作符的情况
        }

    def get_mutate_types(self):
        return ['IndexIncrement', 'IndexDecrement']

    def mutate(self, code: str) -> str:
        tree = ASTParser.parse_to_tree(code)
        if tree is None:
            return code

        collector = ArrayIndexCollector()
        collector.visit(tree)
        index_nodes = collector.index_nodes

        if not index_nodes:
            return code

        target_node = random.choice(index_nodes)
        mutation_type = self.select_mutation_type()

        class IndexTransformer(ast.NodeTransformer):
            def visit_Subscript(self, node):
                if node == target_node:
                    original_index = self._get_index_expression(node)
                    mutated_index = outer_self._mutate_index(node.slice, mutation_type)

                    # 构建变异后的节点
                    new_node = ast.Subscript(
                        value=node.value,
                        slice=mutated_index,
                        ctx=node.ctx
                    )
                    ast.copy_location(new_node, node)

                    # 记录变异信息
                    outer_self.record_mutation(
                        mutator_type="ArrayMutator",
                        mutate_type=mutation_type,
                        line_num=getattr(node, 'lineno', 0),
                        original_code=f"{ASTParser.tree_to_code(node.value)}[{original_index}]",
                        mutated_code=f"{ASTParser.tree_to_code(new_node.value)}[{ASTParser.tree_to_code(new_node.slice)}]",
                        description=f"Array index mutated: {original_index} → {ASTParser.tree_to_code(mutated_index)}"
                    )
                    return new_node
                return node

            def _get_index_expression(self, node):
                if isinstance(node.slice, (ast.Constant, ast.Name)):
                    return ASTParser.tree_to_code(node.slice)
                return ASTParser.tree_to_code(node.slice.value)

        outer_self = self
        mutated_tree = IndexTransformer().visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return ASTParser.tree_to_code(mutated_tree)

    def _mutate_index(self, index_node: ast.AST, mutation_type: str) -> ast.AST:
        if isinstance(index_node, (ast.Constant, ast.Name)):
            return self._handle_simple_index(index_node, mutation_type)
        elif isinstance(index_node, ast.BinOp):
            return self._handle_binary_operation(index_node, mutation_type)
        return index_node

    def _handle_simple_index(self, node: ast.AST, mutation_type: str) -> ast.AST:
        delta = random.randint(1, 3)

        delta = delta if mutation_type == 'IndexIncrement' else -delta

        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return ast.Constant(value=node.value + delta)

        return ast.BinOp(
            left=node,
            op=ast.Add() if mutation_type == 'IndexIncrement' else ast.Sub(),
            right=ast.Constant(value=1)
        )

    def _handle_binary_operation(self, node: ast.BinOp, mutation_type: str) -> ast.AST:
        delta_op = ast.Add() if mutation_type == 'IndexIncrement' else ast.Sub()

        # 嵌套新的运算
        return ast.BinOp(
            left=node,
            op=delta_op,
            right=ast.Constant(value=1)
        )