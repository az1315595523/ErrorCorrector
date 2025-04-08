h = eval(input())
N = eval(input())
L = h
if N==1:
    print("%.2f"%h)
else:
    for i in range(1,N):
        L = L+2*h*0.5**i
    print("%.2f"%L)

