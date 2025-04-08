h=eval(input())
n=eval(input())
H=h
if n==1:
    print('%.2f'%(h))
else:
    for i in range(1,n):
        H=H+2*h*0.5**i
    print('%.2f'%(H))
