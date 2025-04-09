d = float(input())
b = int(input())
d = d
if b > 1:
    for x in range(1, b):
        d = d * (1 / 2) ** x
        d = d + d * 2
    print('%.2f' % d)
else:
    print('%.2f' % d)
