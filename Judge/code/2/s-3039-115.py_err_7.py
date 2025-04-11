b = eval(input())
L = b.copy()
i = max(b)
b = min(b)
for i in b:
    if i == i or i == b:
        L.remove(i)
print(L)
