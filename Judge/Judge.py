import subprocess
import json
import os
import tempfile


class SimpleJudge:
    def __init__(self, test_case_file):
        self.test_cases = self.load_test_cases(test_case_file)
        self.timeout = self.test_cases['timeout']

    @staticmethod
    def load_test_cases(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    def run_test(self, code_path):
        results = []
        for case in self.test_cases['test_cases']:
            try:
                # 创建临时输入文件
                with tempfile.NamedTemporaryFile(mode='w+', delete=False) as input_file:
                    input_file.write(case['input'])
                    input_file.seek(0)

                # 执行代码
                result = subprocess.run(
                    ['python', code_path],
                    stdin=open(input_file.name, 'r'),
                    capture_output=True,
                    text=True,
                    timeout=self.timeout
                )

                # 清理临时文件
                os.unlink(input_file.name)

                # 获取输出
                output = result.stdout.strip()
                error = result.stderr.strip()

                # 判断结果
                passed = output == case['output']
                results.append({
                    'input': case['input'],
                    'expected': case['output'],
                    'actual': output,
                    'passed': passed,
                    'error': error if error else None
                })

            except subprocess.TimeoutExpired:
                results.append({
                    'input': case['input'],
                    'error': 'Timeout'
                })
            except Exception as e:
                results.append({
                    'input': case['input'],
                    'error': f'System error: {str(e)}'
                })

        return results

    def print_result(self, results):
        print(f"评测结果 ({len(results)} 个测试用例)")
        print("=" * 40)

        for i, res in enumerate(results, 1):
            print(f"测试用例 {i}:")
            print(f"输入:\n{res['input']}")
            if 'expected' in res:
                print(f"预期输出: {res['expected']}")
                print(f"实际输出: {res['actual']}")
                print(f"错误信息: {res['error'] or '无'}")
                print(f"状态: {'通过' if res['passed'] else '失败'}")
            else:
                print(f"发生错误: {res['error']}")
            print("-" * 40)

        passed = sum(1 for res in results if res.get('passed', False))
        print(f"最终结果: {passed}/{len(results)} 通过")


if __name__ == "__main__":
    judge = SimpleJudge('test_cases/add_two_numbers.json')
    results = judge.run_test('submissions/user_code.py')
    judge.print_result(results)