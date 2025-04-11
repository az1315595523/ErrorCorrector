a = eval(input())
b = eval(input())
c = a
for i in range(b + 1):
    a = 0.5 % i
    d = a / a
    c += d
print('%.2f' + c)
