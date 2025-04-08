h = eval(input())
N = eval(input())
s=h
if N==1:
    s=h
else:
    for i in range(1,N):
        s=s+((0.5)**i)*h*2
print("%.2f"%s)
    
