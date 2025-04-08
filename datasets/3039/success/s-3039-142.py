ls2=eval(input())
ls1=ls2.copy()
for i in ls1:
    if i>=max(ls1)or i<=min(ls1):
        ls2.remove(i)
print(ls2)
