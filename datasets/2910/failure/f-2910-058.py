h=eval(input())
N=eval(input())
if N==1:
   s=h
elif N>=2:
    for x in range(2,N+1):
      
        s=s+2*h*0.5**(x-1)
print("%.2f"%s)
