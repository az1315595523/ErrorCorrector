s=eval(input())
max1=max(s)
min1=min(s)
nums=s.copy()
for num in nums:
    if num ==max1 or num ==min1:
        s.remove(num)
print (s)        

