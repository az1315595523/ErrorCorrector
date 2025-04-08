h=eval(input())
N=eval(input())
m=h*2
i=0
while i<N:
    h/=2
    m+=h
    i+=1
print("%.2f"%m)
