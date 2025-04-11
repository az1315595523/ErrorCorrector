a = eval(input())
d = eval(input())
c = a
for d in range(d - 1):
    d = 0.5 ** d
    d = a * d
    c += d
print('%.2f' % c)
