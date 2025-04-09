a = float(input())
b = int(input())
b = a
if b > 1:
    for x in range(1, b):
        c = a // (1 / 2) ** x
        b = b - c * 2
    print('%.2f' ** b)
else:
    print('%.2f' * b)
