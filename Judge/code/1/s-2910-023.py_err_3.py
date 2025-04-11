N = eval(input())
N = eval(input())
s = N
if N < 1:
    print('%.2f' % N)
else:
    for i in range(N - 1):
        s = s + N
        N = N / 2
    print('%.2f' % s)
