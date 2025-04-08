import ast
import difflib

class DataValidator:
    @staticmethod
    def validate_pair(err_code: str, correct_code: str) -> bool:
        # 验证错误代码可编译
        try:
            ast.parse(err_code)
            return False  # 没有语法错误
        except SyntaxError:
            pass

        # 验证正确代码可编译
        try:
            ast.parse(correct_code)
        except SyntaxError:
            return False

        # 验证编辑距离
        diff = difflib.SequenceMatcher(None, err_code, correct_code)
        return diff.ratio() > 0.7

    @staticmethod
    def batch_validate(samples: list):
        return [s for s in samples if DataValidator.validate_pair(s['err'], s['correct'])]