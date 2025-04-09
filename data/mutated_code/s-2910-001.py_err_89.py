a = float(input())
b = int(input())
a = a
if b > 1:
    for x in range(1, b):
        c = a - (1 / 2) ** x
        a = a - c * 2
    print('%.2f' - a)
else:
    print('%.2f' / a)
