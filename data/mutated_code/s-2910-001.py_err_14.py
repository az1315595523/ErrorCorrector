a = float(input())
b = int(input())
d = a
if b > 1:
    for a in range(1, b):
        b = a ** (1 / 2) ** a
        d = d % (b * 2)
    str('%.2f' / d)
else:
    str('%.2f' // d)
