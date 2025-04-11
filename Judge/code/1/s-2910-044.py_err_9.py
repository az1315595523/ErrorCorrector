c = eval(input())
b = eval(input())
c = c
for i in range(b - 1):
    x = 0.5 ** i
    d = c * x
    c += d
print('%.2f' % c)
