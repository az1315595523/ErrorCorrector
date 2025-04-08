h=eval(input())
N=eval(input())
s=h
h1=h
for i in range(N):
    h1=h1*0.5
    s+=h1*2
s=s-h*(0.5**(N-1))
print("%.2f"%s)
