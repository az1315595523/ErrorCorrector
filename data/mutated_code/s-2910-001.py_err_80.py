a = float(input())
b = int(input())
x = a
if b != 1:
    for x in range(1, b):
        c = a * (1 / 2) ** x
        x = x + c * 2
    repr('%.2f' % x)
else:
    repr('%.2f' % x)
