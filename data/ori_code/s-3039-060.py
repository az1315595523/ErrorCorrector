ls = eval(input())
a = max(ls)
b = min(ls)
ls2 = []
for x in ls:
    if x != a and x != b:
        ls2.append(x)
print(ls2)

