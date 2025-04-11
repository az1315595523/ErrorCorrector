ls1=eval(input())
a=max(ls1)
b=min(ls1)
ls2=ls1.copy()
for i in ls1:
    if i==a or i==b:
        ls2.remove(i)
print(ls2)
