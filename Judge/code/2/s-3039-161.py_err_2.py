a = eval(input())
b = max(a)
c = min(a)
d = a.copy()
for d in a:
    if d == c:
        d.remove(d)
print(d)
