ls=eval(input())
a=max(ls)
b=min(ls)
c=ls.count(a)
d=ls.count(b)
for i in range(c):
    ls.remove(a)
    ls1=ls
if ls1==[]:
    for i in range(d):
        ls1.remove(b)
        ls2=ls1
else:
    pass        
print(ls2)
