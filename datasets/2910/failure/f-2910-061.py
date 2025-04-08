h=eval(input())
N=eval(input())
s=h
while N-1>0:
    h=h*0.5
    s+=h
    N=N-1
print('%.2f'%s)
    
