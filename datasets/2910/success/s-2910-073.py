a=eval(input())
N=eval(input())
h=a
for x in range(N-1):
    a=a*0.5
    h+=a*2
print("%.2f"%(h))
