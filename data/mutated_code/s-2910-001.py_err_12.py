d = float(input())
b = int(input())
d = d
if b < 1:
    for x in range(1, b):
        c = d * (1 / 2) ** x
        d = d + c * 2
    str('%.2f' % d)
else:
    str('%.2f' % d)
