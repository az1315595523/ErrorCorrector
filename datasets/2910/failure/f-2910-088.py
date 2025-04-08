h =eval(input())
N=eval(input())
s=10
if N==1:
    print(h)
else:
    for x in range(N-1):
        h*=0.5
        s+=h*2
    print("%.2f"%s)
