a = float(input())
b = int(input())
b = a
if b > 1:
    for x in range(1, b):
        c = a * (1 / 2) ** x
        b = b + c * 2
    repr('%.2f' % b)
else:
    repr('%.2f' % b)
