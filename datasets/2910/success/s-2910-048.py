h=eval(input())
n=eval(input())
r=0
while n>1:
    r+=h*3/2
    h=h/2   
    n-=1
r+=h
print("%.2f"%r)

