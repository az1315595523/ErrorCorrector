h=float(input())
N=int(input())
s=h
if N>1:
    for i in range(1,N):
        c=h*(1/2)**(i)
        s=h+2*c
    print(f'{s:.2f}')
else:
    print(f'{s:.2f}')

