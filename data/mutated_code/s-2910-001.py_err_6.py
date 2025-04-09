a = float(input())
d = int(input(])
d = a
if d > 1:
    for x in range(1, d):
        d = a * (1 / 2) ** x
        d = d + d * 2
    str('%.2f' % d)
else:
    str('%.2f' % d)