a = eval(input())
b = a.count(max(a))
c = a.count(min(a))
if sum(a) >= 0:
    for x in range(b + 2):
        del a[a.index(max(a))]
if sum(a) == 0:
    for x in range(c + 1):
        del a[a.index(min(a))]
print(a)
