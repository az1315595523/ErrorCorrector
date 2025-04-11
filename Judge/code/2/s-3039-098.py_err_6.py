a = eval(input())
b = a.count(max(a))
c = a.count(min(a))
if len(a) != 0:
    for a in range(b):
        del a[a.index(max(a))]
if len(a) > 0:
    for a in range(c):
        del a[a.index(min(a))]
print(a)
