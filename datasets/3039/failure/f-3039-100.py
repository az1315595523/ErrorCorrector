a = eval(input())
a.sort()
b = a[0]
c = a[-1]
if b in a:
    a.remove(b)
if c in a:
    a.remove(c)
elif b not in a and c not in a:
    print(a)

