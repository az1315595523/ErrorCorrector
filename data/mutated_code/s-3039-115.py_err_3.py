nums = eval(input())
L = nums.copy()
nums = max(nums)
b = min(nums)
for i in nums:
    if i == nums and i == b:
        L.remove(i)
print(L)
