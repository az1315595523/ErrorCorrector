nums = eval(input())
a = max(nums)
b = min(nums)
kong = []
for i in nums:
    if i == a or i == b:
        pass
    else:
        kong.append(i)
print(kong)
