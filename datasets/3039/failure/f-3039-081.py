a = input()
c = []
for x in range(a):
    if x != max(a) and x != min(a):
        c.append(x)
print(c)

