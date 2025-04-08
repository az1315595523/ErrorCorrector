h=float(input())
N=int(input())
s=h
if N>1:
    for i in range(1,N):
        s=h+2*(h/2**(i))
        print(f'{s:.2f}')
else:
    print(f'{s:.2f}')

