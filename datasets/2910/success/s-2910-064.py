h = int(input())
n = int(input())
s = h
for i in range(n-1):
    h = h * (0.5)
    s = s + 2 * h
print('%.2f'%s)
