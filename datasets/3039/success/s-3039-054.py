a=eval(input())
b =[]
for x in a:
    if x != max(a) and x!=min(a):
        b.append(x)
print(b)

