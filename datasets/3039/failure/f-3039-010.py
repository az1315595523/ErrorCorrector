ls=eval(input())
b=max[ls]
a=ls.count(b)
for i in range(a):
    ls.remove(b)
c=min[ls]
d=ls.count(c)
for i in range(d):
    ls.remove(c)
print(ls)
