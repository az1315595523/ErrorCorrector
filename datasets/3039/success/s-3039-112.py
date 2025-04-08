a=eval(input())
b=max(a)
c=min(a)
d=[]
for i in a:
    if i!=b and i!=c:
        d.append(i)
print(d)
