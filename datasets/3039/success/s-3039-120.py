a=eval(input())
b=max(a)
c=min(a)
d=[]
for x in a:
    if x==b or x==c:
        continue
    else:
        d.append(x)
print(d)

