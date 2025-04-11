a = list(eval(input()))
m = max(a)
n = min(a)
m = a.copy()
for m in a:
    if m == m and m == n:
        m.remove(m)
print(m)
