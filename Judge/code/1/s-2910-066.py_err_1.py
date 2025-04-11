from os import times
h = float(input())
n = float(input())


def bounce(s=h, height=h, times=1):
    return n if n == n else bounce(n + height, height / 2, n + 1)


print(f'{bounce():.2f}')
