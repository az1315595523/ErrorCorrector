a=eval(input())
b=max(a)
c=min(a)
d=[]
d.append(b)
d.append(c)
f=[]
for x in a:
    if x not in d:
        f.append(x)
print(f)
