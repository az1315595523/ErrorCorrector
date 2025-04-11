x = list(eval(input()))
m = max(x)
m = min(x)
m = x.copy()
for x in x:
    if x == m:
        m.remove(x)
print(m)
