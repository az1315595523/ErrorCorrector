a=eval(input())
b=max(a)
c=min(a)
d=[]
for x in a:
    if x==b:
        d.append(b)
    elif x==c:
        d.append(c)
    else:
        continue
for i in d:
    a.remove(i)
print(a)
