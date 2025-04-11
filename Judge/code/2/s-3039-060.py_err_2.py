a = eval(input())
a = max(a)
b = min(a)
a = []
for x in a:
    if x != b:
        a.append(x)
print(a)
