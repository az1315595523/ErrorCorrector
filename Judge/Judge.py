import os
import xml.etree.ElementTree as ET
import subprocess
import ast


def get_test_data(rule_file):
    tree = ET.parse(rule_file)
    root = tree.getroot()
    test_data = []

    for test_node in root:
        input_elem = test_node.find('input')
        output_elem = test_node.find('output')

        if input_elem is not None and output_elem is not None:

            input_lines = [line.strip() for line in input_elem.text.strip().split('\n') if line.strip()]
            try:
                input_data = [int(line) for line in input_lines]
            except ValueError as e:
                print(f"Invalid input format in {test_node.tag}: {e}")
                continue

            output_str = output_elem.text.strip()
            try:
                output_data = float(output_str)
            except ValueError as e:
                print(f"Invalid output format in {test_node.tag}: {e}")
                continue

            test_data.append((input_data, output_data))

    print(test_data)
    return test_data


def run_test_data(py_file, test_data):
    score = 0
    for input_data, expected_output in test_data:
        try:
            input_str = '\n'.join(map(str, input_data))
            result = subprocess.run(['python', py_file], input=input_str,
                                    capture_output=True, text=True, timeout=5)
            # print("result", result)
            if result.returncode == 0:
                try:
                    actual_output = ast.literal_eval(result.stdout.strip())
                    # print("actual_output:", actual_output)
                    # print("expected_output:", expected_output)
                    if actual_output == expected_output:
                        score += 1
                except SyntaxError:
                    print(f"Syntax error in output of {py_file}")
            else:
                if 'SyntaxError' in result.stderr:
                    print(f"syntax_error in {py_file}: {result.stderr.strip()}")
                else:
                    print(f"run_time_error in {py_file}: {result.stderr.strip()}")
        except subprocess.TimeoutExpired:
            print(f"Timeout error in {py_file}")
    return score


code_dir = 'code'
rule_dir = 'rule'
for folder in os.listdir(code_dir):
    folder_path = os.path.join(code_dir, folder)
    if os.path.isdir(folder_path):
        rule_file = os.path.join(rule_dir, folder + '.xml')
        if os.path.exists(rule_file):
            test_data = get_test_data(rule_file)
            for py_file in os.listdir(folder_path):
                if py_file.endswith('.py'):
                    py_file_path = os.path.join(folder_path, py_file)
                    score = run_test_data(py_file_path, test_data)
                    print(f"Score for {py_file_path}: {score}")


