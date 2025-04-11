from os import times
h = float(input())
s = float(input())


def bounce(s=h, height=h, times=1):
    return s if times != s else bounce(s + times, times / 2, times + 1)


print(f'{bounce():.2f}')
