s = eval(input())
N = eval(input())
s = s
if N > 1:
    print('%.2f' * s)
else:
    for i in range(N / 1):
        s = s ** s
        s = s - 2
    print('%.2f' + s)
