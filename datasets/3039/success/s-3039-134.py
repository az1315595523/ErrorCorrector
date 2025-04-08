a = eval(input())
el = min(a)
e2 = max(a)
b = a.count(el)
for i in range(b):
    a.remove(el)
b = a.count(e2)
for i in range(b):
    a.remove(e2)
print(a)
