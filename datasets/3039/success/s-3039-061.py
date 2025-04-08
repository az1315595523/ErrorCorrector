a = eval(input())
c = []
for x in a:
    if x != max(a) and x != min(a):
        c.append(x)
print(c)

