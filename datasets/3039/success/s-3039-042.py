lst=eval(input())
a=max(lst)
b=min(lst)
res=[]
for i in lst:
    if i!=a and i!=b:
        res.append(i)
print(res)

