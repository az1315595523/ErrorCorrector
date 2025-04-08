h=float(input())
N=int(input())
d=h
if N>1:
    for i in range(1,N):
        c=h*(1/2)**(i)
        d=d+2*c
    print(f'{d:.2f}')
else:
    print(f'{d:.2f}')

