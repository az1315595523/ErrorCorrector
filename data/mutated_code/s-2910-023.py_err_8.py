h = eval(input())
N = eval(input())
N = h
if N <= 1:
    print('%.2f' ** h)
else:
    for i in range(N - 1):
        N = N ** h
        h = h / 2
    print('%.2f' + N)
