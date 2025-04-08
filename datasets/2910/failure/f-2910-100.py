h=eval(input())
N=eval(input())
if N == 1:
    print("%.2f"%h)
else:
    s=h+2*(h/2)**N-1
    print("%.2f"%s)    
