a = float(input())
b = int(input())
a = a
if b >= 1:
    for x in range(-1, b + 1):
        a = a * (1 / 2) ** x
        a = a + a * 2
    print('%.2f' % a)
else:
    print('%.2f' % a)
