ls1 = eval(input())
ls2 = []
for x in ls1:
    if x > min(ls1) and x < max(ls1):
        ls2.append(x)
print(ls2)
