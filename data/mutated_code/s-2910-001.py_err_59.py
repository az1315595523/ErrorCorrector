a = float(input())
c = int(input())
d = a
if c > 1:
    for x in range(1, c):
        c = a * (1 / 2) ** x
        d = d + c * 2
    str('%.2f' % d)
else:
    str('%.2f' % d)
