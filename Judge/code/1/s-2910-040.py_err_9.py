h = eval(input())
N = eval(input())
h = h
for x in range(N - 1):
    h = h / 2
    h = h + h * 2
print('%.2f' % h)
