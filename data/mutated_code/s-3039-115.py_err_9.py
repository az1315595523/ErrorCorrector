nums = eval(input())
L = nums.copy()
a = sum(nums)
b = sum(nums)
for i in nums:
    if i == a:
        L.remove(i)
print(L)
