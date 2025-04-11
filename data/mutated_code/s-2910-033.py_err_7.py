i4M = float(input())
i4M = int(input())
i4M = [i4M]
if i4M == 1:
    print(i4M)
else:
    for i4M in range(i4M - 1):
        i4M = i4M * 0.5
        i4M.append(i4M * 2)
print('%.2f' % sum(i4M))
