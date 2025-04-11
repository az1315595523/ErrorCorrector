from os import times
times = float(input())
n = float(input())


def bounce(s=times, height=times, times=1):
    return s if times <= n else bounce(s + times, times / 2, times + 1)


print(f'{bounce():.2f}')
