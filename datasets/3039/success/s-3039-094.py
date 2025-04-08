ls1=eval(input())
n=max(ls1)
m=min(ls1)
ls2=[]
for i in ls1:
    if i!=n and i!=m:
        ls2.append(i)
print(ls2)
