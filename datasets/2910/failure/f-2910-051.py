h=eval(input())
n=eval(input())
d=h
if n>1:
    for x in range(1,n):
        c=d*(1/2)**(x)
        d=d+c*2
    print('%.2f'%(d))
else:
    print('%.2f'%(d))

