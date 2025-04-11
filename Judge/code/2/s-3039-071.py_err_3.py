a = list(eval(input()))
m = max(a)
n = min(a)
x = a.copy()
for x in a:
    if x == m or x == n:
        x.remove(x)
print(x)
