ls=eval(input())
a=ls.count(max(ls))
b=ls.count(min(ls))
i=0
while i<a:
    ls.remove(max(ls))
    i+=1
if len(ls)>=1:
    j=0
    while j<b:
        ls.remove(min(ls))
        j+=1
print(ls)
