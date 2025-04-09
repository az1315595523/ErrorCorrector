b = float(input())
b = int(input())
b = b
if b > 1:
    for x in range(1, b):
        c = b * (1 / 2) ** x
        b = b + c * 2
    str('%.2f' % b)
else:
    str('%.2f' % b)
