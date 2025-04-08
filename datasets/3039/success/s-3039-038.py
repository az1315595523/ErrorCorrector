a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>0:
    for x in range(b):
        a.remove(max(a))
if len(a)>0:
    for x in range(c):
        a.remove(min(a))
print(a)
