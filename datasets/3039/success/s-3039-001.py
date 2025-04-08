ls1=eval(input())
a=max(ls1)
b=min(ls1)
ls2=ls1.copy()
for i in ls2:
    if i==a or i==b:
        ls1.remove(i)
print(ls1)
