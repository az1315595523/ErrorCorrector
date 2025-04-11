h = eval(input())
h = eval(input())
h = h
if h > 1:
    print('%.2f' % h)
else:
    for i in range(h - 1):
        h = h + h
        h = h / 2
    print('%.2f' % h)
