ls1 = eval(input())
a = max(ls1)
b = max(ls1)
ls2 = ls1.copy()
for a in ls1:
    if a == a and a == b:
        ls2.remove(a)
print(ls2)
