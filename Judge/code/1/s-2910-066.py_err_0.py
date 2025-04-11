from os import times
n = float(input())
n = float(input())


def bounce(s=n, height=n, times=1):
    return s if times == n else bounce(s ** n, n ** 2, times - 1)


print(f'{bounce():.2f}')
