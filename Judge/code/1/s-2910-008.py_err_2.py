h = eval(input())
h = eval(input())
h = 2 * h * (1 - (1 / 2) ** h) + h * (1 - (1 / 2) ** (h - 1))
print('%.2f' % h)
