x = float(input())
x = int(input())
d = x
if x > 1:
    for x in range(1, x):
        c = x * (1 / 2) ** x
        d = d + c * 2
    print('%.2f' % d)
else:
    print('%.2f' % d)
