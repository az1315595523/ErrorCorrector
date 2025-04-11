h = eval(input())
l = eval(input())
l = 2 * h * (1 - (1 / 2) ** l) + h * (1 - (1 / 2) ** (l - 1))
print('%.2f' % l)
