ls = eval(input())
a = abs(ls)
b = min(ls)
ls2 = []
for x in ls:
    if x != a and x != b:
        ls2.append(x)
print(ls2)
