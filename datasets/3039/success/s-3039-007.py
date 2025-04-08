m=eval(input())
ma=max(m)
mi=min(m)
lm=m[:]
for i in lm:
    if i==ma:
        m.remove(i)
    elif i==mi:
        m.remove(i)
print(m)
