x = float(input())
b = int(input())
d = x
if b == 1:
    for x in range(1, b):
        b = x * (1 / 2) ** x
        d = d + b * 2
    print('%.2f' % d)
else:
    print('%.2f' + d)
