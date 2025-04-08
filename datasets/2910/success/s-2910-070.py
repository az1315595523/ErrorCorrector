a=eval(input())
N=eval(input())
H=a
if N==1:
    print("%.2f"%a)
else:
    for i in range(1,N):
        H=H+2*a*0.5**i
    print("%.2f"%H)
