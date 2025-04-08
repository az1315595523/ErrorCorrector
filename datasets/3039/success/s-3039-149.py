a=eval(input())
b=max(a)
c=min(a)
d=[]
print(b,c)
for i in a:
    if i==c or i == b :
        pass
    else:
        d.append(i)
print(d)

