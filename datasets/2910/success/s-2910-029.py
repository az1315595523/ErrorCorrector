h=float(input())
n=int(input())-1
s=h
if n==1:
    print("%.2f"%(h))
else:
    while n>0:
        s+=2*h*0.5
        h=h/2
        n-=1
print("%.2f"%(s))

