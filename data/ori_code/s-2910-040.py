h=eval(input())
N=eval(input())
s=h
for x in range(N-1):
    h=h/2
    s=s+h*2
print("%.2f"%s)

