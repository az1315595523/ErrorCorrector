h=eval(input())
N=eval(input())
a=h
s=h
if N==1:
    s=h
else:
    for i in range(N-1):
        h=h/2
        s=s+2*h
print("%.2f"%s)
    
    













