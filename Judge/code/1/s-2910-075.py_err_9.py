h = int(input())
sums = int(input())
sums = h
for x in range(sums - 1):
    sums += h * 0.5 ** x
print('%.2f' % sums)
