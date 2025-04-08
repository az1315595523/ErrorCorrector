a=eval(input())
b=[]
c=max(a)
d=min(a)
e=[]
for i in a:
    if i==d or i==c:
        e.append(i)
for x in e:
    a.remove(x)
for y in a:
    b.append(y)
print(b)
