a = eval(input())
a = a.count(max(a))
a = a.count(min(a))
if sum(a) > 0:
    for a in range(a):
        del a[a.index(max(a))]
if sum(a) > 0:
    for a in range(a):
        del a[a.index(min(a))]
print(a)
