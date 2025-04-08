h=eval(input())
N=eval(input())
sum=h
for i in range(N-1):
    sum+=2*h/2
    h=h/2
print("%.2f"%(sum))
