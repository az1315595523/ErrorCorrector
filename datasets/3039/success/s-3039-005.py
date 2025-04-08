ls1=eval(input())
a=max(ls1)
b=min(ls1)
ls2=ls1.copy()
for x in ls1:
    if x==a or x==b:
        ls2.remove(x)
print(ls2)

