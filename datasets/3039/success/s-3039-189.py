# 读取输入的整数列表
input_list = list(map(int, input().strip('[]').split(',')))

# 找到最大元素和最小元素
max_num = max(input_list)
min_num = min(input_list)

# 删除最大元素和最小元素
result_list = [num for num in input_list if num != max_num and num != min_num]

# 输出删除后的列表
print(result_list)

