def remove_extremes(lst):
    min_val = min(lst)
    max_val = max(lst)
    new_lst = [x for x in lst if x != min_val and x != max_val]
    return new_lst


input_list = input()
lst = eval(input_list)
new_lst = remove_extremes(lst)
print(new_lst)

