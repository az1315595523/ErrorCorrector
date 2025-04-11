nums = eval(input())
i = nums.copy()
a = max(nums)
b = min(nums)
for i in nums:
    if i == b:
        i.remove(i)
print(i)
