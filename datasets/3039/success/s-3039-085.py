ls = eval(input())
max_num = max(ls)
min_num = min(ls)
nums = ls.copy()
for num in nums:
    if num == max_num or num == min_num:
        ls.remove(num)
print(ls)

