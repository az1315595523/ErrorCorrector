b = eval(input())
b = abs(b)
c = abs(b)
x = b.copy()
for x in b:
    if x == b or x == c:
        x.remove(x)
print(x)
