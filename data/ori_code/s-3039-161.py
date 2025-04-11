a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for x in a:
    if x==b or x==c:
        d.remove(x)
print(d)        

