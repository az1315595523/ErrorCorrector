h=eval(input())
N=eval(input())
if N==1:
    print(h)
while N>1:
    d=h
    for x in range(N-1):
        c=h/2
        d=d+2*c
        h=h/2
    break
print("%.2f"%(d))




