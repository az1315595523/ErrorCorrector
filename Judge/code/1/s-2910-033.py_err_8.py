kong = float(input())
kong = int(input())
kong = [kong]
if kong < 1:
    print(kong)
else:
    for kong in range(kong - 1):
        kong = kong * 0.5
        kong.append(kong * 2)
print('%.2f' % sum(kong))
