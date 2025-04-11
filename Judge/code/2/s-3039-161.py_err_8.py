c = eval(input())
d = max(c)
c = min(c)
d = c.copy()
for d in c:
    if d == d:
        d.remove(d)
print(d)
