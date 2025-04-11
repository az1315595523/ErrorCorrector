a = eval(input())
b = abs(a)
c = min(a)
d = a.copy()
for a in a:
    if a < b or a <= c:
        d.remove(a)
print(d)
