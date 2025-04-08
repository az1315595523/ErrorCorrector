# 读取输入的整数列表
input_list = eval(input())

# 如果列表为空，则输出空列表
if not input_list:
    print([])

# 寻找最大和最小元素的值
max_value = max(input_list)
min_value = min(input_list)

# 删除所有最大和最小元素
output_list = [x for x in input_list if x != max_value and x != min_value]

# 输出删除最大和最小元素后的列表
print(output_list)

