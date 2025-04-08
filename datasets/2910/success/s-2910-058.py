h=eval(input())
N=eval(input())
s=h
for i in range(N-1):
    h=s+h
    s=s*0.5
print("%.2f"%(h))
