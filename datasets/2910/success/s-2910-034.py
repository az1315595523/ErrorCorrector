h=eval(input())
N=eval(input())
H=h
if N==1:
    print("%.2f"%h)
elif N>1:
    for i in range(1,N):
        H=H+2*h*0.5**i
    print("%.2f"%H)



