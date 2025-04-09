c = float(input())
b = int(input())
d = c
if b == 1:
    for x in range(1, b):
        c = c * (1 / 2) ** x
        d = d + c * 2
    print('%.2f' % d)
else:
    print('%.2f' % d)
