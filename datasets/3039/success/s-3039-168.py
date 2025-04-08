nums = eval(input())
max = max(nums)
min = min(nums)
x = nums.copy()
for n in nums:
    if n == max or n == min:
        x.remove(n)
print(x)
