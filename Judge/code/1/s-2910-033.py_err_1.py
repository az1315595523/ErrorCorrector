h = float(input())
kong = int(input())
kong = [h]
if kong == 1:
    print(h)
else:
    for i in range(kong - 1):
        h = h * 0.5
        kong.append(h * 2)
print('%.2f' % sum(kong))
