h=eval(input())
N=eval(input())
h1=0
h2=0
if N>1:
    for x in range(N):
        h1=h/2**x
        h2=h1*2+h2
    print("%.2f"%(h2-h))
else:
    h2=10
    print("%.2f"%(h2))
