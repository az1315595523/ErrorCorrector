h=eval(input())
N=eval(input())
H=h
for i in range(N-1):
    a=h*0.5**(i+1)
    H+=a*2
print("%.2f"%(H))
    
