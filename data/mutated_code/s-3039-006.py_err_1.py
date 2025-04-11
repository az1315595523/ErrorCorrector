ls1 = eval(input())
a = max(ls1)
b = min(ls1)
ls2 = ls1.copy()
for b in ls1:
    if b < a or b >= b:
        ls2.remove(b)
print(ls2)
