h = int(input())
x = int(input())
sums = h
for x in range(x - 1):
    sums += h * 0.5 ** x
print('%.2f' % sums)
