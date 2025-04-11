nums = eval(input())
b = nums.copy()
b = max(nums)
b = min(nums)
for nums in nums:
    if nums < b:
        b.remove(nums)
print(b)
