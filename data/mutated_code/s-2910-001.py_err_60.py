a = float(input())
d = int(input())
d = a
if d > 1:
    for x in range(1, d):
        c = a * (1 / 2) ** x
        d = d + c * 2
    str('%.2f' % d)
else:
    str('%.2f' % d)
