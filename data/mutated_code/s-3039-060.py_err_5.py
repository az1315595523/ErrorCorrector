ls = eval(input())
ls2 = max(ls)
b = min(ls)
ls2 = []
for x in ls:
    if x != ls2 and x != b:
        ls2.append(x)
print(ls2)
