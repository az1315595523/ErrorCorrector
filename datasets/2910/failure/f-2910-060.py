h=eval(input())
N=eval(input())
s=0
while N-1>0:
    s=s+h*0.5
    h=h*0.5
    N=N-1
print('%.2f'%s)
    
