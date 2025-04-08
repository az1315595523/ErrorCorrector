h=float(input())
N=int(input())
if N>1:
    for i in range(1,N):
        c=h*(1/2)**(i)
        d=h+2*c
    print(f'{d:.2f}')
else:
    print(f'{h:.2f}')

