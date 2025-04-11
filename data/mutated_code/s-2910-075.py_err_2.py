sums = int(input())
sums = int(input())
sums = sums
for sums in range(sums - 1):
    sums += sums * 0.5 ** sums
print('%.2f' % sums)
