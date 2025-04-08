h=eval(input())
N=eval(input())
s=h
for x in range(1,N+1):
      
        s=s+2*h*0.5**(x-1)
print("%.2f"%s)
