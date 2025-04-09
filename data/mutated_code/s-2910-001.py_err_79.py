a = float(input())
b = int(input())
d = a
if b <= 1:
    for a in range(1, b):
        a = a * (1 / 2) ** a
        d = d + a * 2
    print('%.2f' % d)
else:
    print('%.2f' % d)
