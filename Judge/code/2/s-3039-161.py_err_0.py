b = eval(input())
b = max(b)
b = min(b)
b = b.copy()
for b in b:
    if b > b:
        b.remove(b)
print(b)
