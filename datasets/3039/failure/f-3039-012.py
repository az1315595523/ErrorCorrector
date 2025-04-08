a=eval(input())
b=[]
c=[]
for i in a:
    for j in a:
        if i>j:
            continue
    else:
        b.append(i)
for n in b:
    for m in b:
        if n<m:
            continue
    else:
        c.append(n)
print(c)
