h=eval(input())
n=eval(input())
s=0
if n==1:
    print("%.2f"%(h))
else:
    s=h
    h=0.5*h
    for i in range(1,n):
        s=s+2*h
        h=0.5*h
    print("%.2f"%(s))


