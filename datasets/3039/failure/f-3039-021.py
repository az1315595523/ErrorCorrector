a=eval(input())
b=max(a)
c=min(a)
for i in a:
    if i==b:
       a.remove(b)
for t in a:
    if t==c:
        a.remove(c)
print(a)
