h=eval(input())
N=eval(input())
s=h
if N==1:
    print("%.2f"%h)
else:
    for i in range(N-1):
        s=s+h
        h=h/2
    print("%.2f"%s)

