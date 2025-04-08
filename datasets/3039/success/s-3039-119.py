a=eval(input())
b=max(a)
c=min(a)
m=[]
m.append(b)
m.append(c)
f=[]
for x in a:
    if x not in m:
        f.append(x)
print(f)
