x=eval(input())
a=x.count(max(x))
b=x,count(min(x))
if len(x)>0:
    for i in range(a):
        del x[x.index(max(x))]
if len(x)>0:
    for i in range(b):
        del x[x.index(min(x))]
print(x)
