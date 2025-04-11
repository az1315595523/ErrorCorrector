nums = eval(input())
L = nums.copy()
a = max(nums)
b = min(nums)
for i in nums:
    if i > b:
        L.remove(i)
print(L)
