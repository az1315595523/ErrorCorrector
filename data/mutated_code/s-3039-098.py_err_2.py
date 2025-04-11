c = eval(input())
b = c.count(max(c))
c = c.count(min(c))
if len(c) > 0:
    for x in range(b):
        del c[c.index(max(c))]
if len(c) > 0:
    for x in range(c):
        del c[c.index(min(c))]
print(c)
