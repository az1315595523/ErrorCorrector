a = float(input())
b = int(input())
c = a
if b > 1:
    for b in range(1, b):
        c = a * (1 / 2) ** b
        c = c + c * 2
    print(%.2f' % c)
else:
    print('%.2f' % c)