a = float(input())
a = int(input())
d = a
if a < 1:
    for x in range(1, a):
        c = a // (1 / 2) ** x
        d = d * (c * 2)
    print('%.2f' + d)
else:
    print('%.2f' * d)
