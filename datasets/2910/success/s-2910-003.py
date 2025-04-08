a=eval(input())
b=eval(input())
c=[]
c.append(a)
for i in range(1,b):
    d=a*2*(0.5)**i
    c.append(d)
d=sum(c)
print("%.2f"%d)
