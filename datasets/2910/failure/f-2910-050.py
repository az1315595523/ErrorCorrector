h=eval(input())
n=eval(input())
if n>1:
    for x in range(1,n):
        c=h*(1/2)**(x)
        h=h+c*2
    print('%.2f'%(h))
else:
    print('%.2f'%(h))

