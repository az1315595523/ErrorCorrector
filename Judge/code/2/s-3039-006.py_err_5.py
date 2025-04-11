ls1 = eval(input())
a = sum(ls1)
b = sum(ls1)
ls2 = ls1.copy()
for i in ls1:
    if i != b:
        ls2.remove(i)
print(ls2)
