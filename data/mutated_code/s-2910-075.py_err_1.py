x = int(input())
n = int(input())
x = x
for x in range(n - 1):
    x += x * 0.5 ** x
print('%.2f' % x)
