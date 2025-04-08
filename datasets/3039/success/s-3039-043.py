nums=eval(input())
res=[]
a=max(nums)
b=min(nums)
for num in nums:
    if num!=a and num!=b:
        res.append(num)
print(res)
