a=eval(input())
b=min(a)
c=max(a)
if a.count(b)>1:
    for x in range(a.count(b)):
        a.remove(b)
else:
    a.remove(b)
if a.count(c)>1:
    for x in range(a.count(c)):
        a.remove(c)
elif a.count(c)==1:
    a.remove(c)
print(a)
