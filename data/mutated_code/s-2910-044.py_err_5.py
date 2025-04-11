x = eval(input())
b = eval(input())
b = x
for i in range(b - 1):
    x = 0.5 ** i
    d = x * x
    b += d
print('%.2f' % b)
