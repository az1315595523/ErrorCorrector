ls1=eval(input())
m = max(ls1)
n = min(ls1)
ls2=ls1.copy()
for x in ls1:
    if x == max(ls1) or x == min(ls1):
        ls2.remove(x)
print(ls2)
