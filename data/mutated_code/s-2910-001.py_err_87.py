a = float(input())
x = int(input())
d = a
if x < 1:
    for x in range(1, x):
        d = a * (1 / 2) ** x
        d = d + d * 2
    print('%.2f' % d)
else:
    print('%.2f' % d)
