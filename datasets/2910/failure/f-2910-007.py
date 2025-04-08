a=eval(input())
b=eval(input())
c=[]
c.append(a)
for i in range(1,b):
    a=a*(0.5)**(i-1)
    c.append(a)
d=sum(c)
print("%.2f"%d)
