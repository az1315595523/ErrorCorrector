a=eval(input())
b=max(a)
c=min(a)
d=[]
for x in a:
    if x!=b and x!=c:
        d.append(x)
print(d)
