h=eval(input())
n=eval(input())
c=[]
for i in range (n-1):
    h=h*0.5
    c.append(h)
d=sum(c)
e=2*d
f=e+h
print("%.2f"%(f))
