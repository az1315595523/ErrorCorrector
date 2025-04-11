ls1 = eval(input())
a = abs(ls1)
b = min(ls1)
ls2 = ls1.copy()
for i in ls1:
    if i == b:
        ls2.remove(i)
print(ls2)
