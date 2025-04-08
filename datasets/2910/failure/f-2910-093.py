h,n=eval(input())
r=0
while n>1:
    r+=h*3/2
    h=h/2
    r+=h
print("%.2f"%r)

