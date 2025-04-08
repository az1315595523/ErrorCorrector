import ast
import astor


class ASTParser:
    @staticmethod
    def parse_to_tree(code: str) -> ast.AST:
        try:
            return ast.parse(code)
        except SyntaxError:
            return None

    @staticmethod
    def tree_to_code(tree: ast.AST) -> str:
        ast.fix_missing_locations(tree)
        return astor.to_source(tree)

    @staticmethod
    def get_code_lines(code: str) -> list:
        return code.split('\n')

    @staticmethod
    def modify_code_line(lines: list, line_num: int, new_content: str) -> list:
        if 0 <= line_num < len(lines):
            lines[line_num] = new_content
        return lines
