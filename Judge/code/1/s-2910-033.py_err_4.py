i = float(input())
i = int(input())
i = [i]
if i == 1:
    print(i)
else:
    for i in range(i - 1):
        i = i * 0.5
        i.append(i * 2)
print('%.2f' % sum(i))
