ls=eval(input())
b=max(ls)
c=min(ls)
nums=ls.copy()
for i in nums:
    if i==b or i==c:
        ls.remove(i)   
print(ls)
