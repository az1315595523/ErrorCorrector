import ast
import random
from ASTParser import ASTParser
from mutators.BaseMutator import BaseMutator


class BoundaryMutator(BaseMutator):
    def __init__(self):
        super().__init__()
        self.original_code = None

    def get_mutate_types(self):
        return [
            'RangeStopInc',
            'RangeStopDec',
            'RangeStartInc',
            'RangeStartDec',
            'RangeStepInc',
            'RangeStepDec'
        ]

    def shift_boundary(self, mutate_type, node):
        shiftScale = random.randint(1, 3)
        args = node.args
        if mutate_type == 'RangeStopInc':
            if isinstance(args[1], ast.Constant):
                args[1].value += shiftScale
            elif isinstance(args[1], ast.Name):
                args[1] = ast.BinOp(left=args[1], op=ast.Add(), right=ast.Constant(value=shiftScale))
        elif mutate_type == 'RangeStopDec':
            if isinstance(args[1], ast.Constant):
                args[1].value -= shiftScale
            elif isinstance(args[1], ast.Name):
                args[1] = ast.BinOp(left=args[1], op=ast.Sub(), right=ast.Constant(value=shiftScale))
        elif mutate_type == 'RangeStartInc':
            if isinstance(args[0], ast.Constant):
                args[0].value += shiftScale
            elif isinstance(args[0], ast.Name):
                args[0] = ast.BinOp(left=args[0], op=ast.Add(), right=ast.Constant(value=shiftScale))
        elif mutate_type == 'RangeStartDec':
            if isinstance(args[0], ast.Constant):
                args[0].value -= shiftScale
            elif isinstance(args[0], ast.Name):
                args[0] = ast.BinOp(left=args[0], op=ast.Sub(), right=ast.Constant(value=shiftScale))
        elif mutate_type == 'RangeStepInc':
            if len(args) > 2 and isinstance(args[2], ast.Constant):
                args[2].value += shiftScale
            elif len(args) > 2 and isinstance(args[2], ast.Name):
                args[2] = ast.BinOp(left=args[2], op=ast.Add(), right=ast.Constant(value=shiftScale))
        elif mutate_type == 'RangeStepDec':
            if len(args) > 2 and isinstance(args[2], ast.Constant):
                args[2].value -= shiftScale
            elif len(args) > 2 and isinstance(args[2], ast.Name):
                args[2] = ast.BinOp(left=args[2], op=ast.Sub(), right=ast.Constant(value=shiftScale))

        self.record_mutation(
            mutator_type="OperatorMutator",
            mutate_type=mutate_type,
            line_num=getattr(node, 'lineno', 0),
            original_code=self.original_code,
            mutated_code=ASTParser.tree_to_code(node),
            description=f"{mutate_type} {shiftScale}"
        )
        return node

    def mutate(self, code: str) -> str:

        tree = ASTParser.parse_to_tree(code)

        outer_self = self

        class BoundaryTransformer(ast.NodeTransformer):
            def visit_For(self, node):
                self.generic_visit(node)
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func,
                                                                  ast.Name) and node.iter.func.id == 'range':
                    args = node.iter.args
                    outer_self.original_code = ASTParser.tree_to_code(node.iter)
                    mutate_types = outer_self.get_mutate_types()

                    if len(args) == 1:
                        mutate_types = mutate_types[2:3]
                        mutate_type = random.choice(mutate_types)
                    elif len(args) == 2:
                        mutate_types = mutate_types[0:4]
                        mutate_type = random.choice(mutate_types)
                    else:
                        mutate_types = mutate_types[0:5]
                        mutate_type = random.choice(mutate_types)
                    outer_self.successful = True
                    return outer_self.shift_boundary(mutate_type, node.iter)

                return node

        transformer = BoundaryTransformer()
        mutated_tree = transformer.visit(tree)

        return ASTParser.tree_to_code(mutated_tree)
