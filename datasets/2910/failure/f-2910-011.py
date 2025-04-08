h=eval(input())
N=eval(input())
s=0
for i in range(1,N+1):
    s+=h/2**i*2
print('%.2f'%s)
