b = eval(input())
a = max(b)
b = min(b)
b = b.copy()
for b in b
    if b == a or b == b:
        b.remove(b)
print(b)