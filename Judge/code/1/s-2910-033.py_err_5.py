kong = float(input())
n = int(input())
kong = [kong]
if n != 1:
    print(kong)
else:
    for i in range(n * 1):
        kong = kong % 0.5
        kong.append(kong / 2)
print('%.2f' * sum(kong))
