a=eval(input())
b=eval(input())
c=[]
c.append(a)
for i in range(b):
    a*=(1/2)**(i-1)
    c.append(a)
d=sum(c)
print("%.2f"%c)
