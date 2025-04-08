input_list = eval(input().strip())
max_value = max(input_list)
min_value = min(input_list)
output_list = [num for num in input_list if num != max_value and num != min_value]
print(output_list)


