h = eval(input())
N = eval(input())
x = h
for x in range(N - 1):
    h = h / 2
    x = x + h * 2
print('%.2f' % x)
