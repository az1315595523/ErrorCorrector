d = eval(input())
b = eval(input())
c = d
for c in range(b - 1):
    x = 0.5 ** c
    d = d * x
    c += d
print('%.2f' % c)
