a = eval(input())
b = a.count(max(a))
c = a.count(min(a))
if len(a) > 0:
        for x in range(b):
                del a[a.index(max(a))]
if len(a) > 0:
        for x in range(b):
                del a[a.index(max(a))]
print(a)
