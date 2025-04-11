s = eval(input())
s = eval(input())
s = s
if s == 1:
    print('%.2f' % s)
else:
    for i in range(s - 1):
        s = s + s
        s = s / 2
    print('%.2f' % s)
