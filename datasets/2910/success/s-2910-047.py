h=eval(input())
N=eval(input())
m=h
for i in range(N-1):
    m+=h*(0.5)**(i)
print("%.2f"%m)
