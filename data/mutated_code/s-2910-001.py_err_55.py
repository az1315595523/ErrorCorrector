a = float(input())
b = int(input())
d = a
if b > 1:
    for b in range(1, b):
        c = a * (1 / 2) ** b
        d = d + c * 2
    repr('%.2f' % d)
else:
    repr('%.2f' % d)
