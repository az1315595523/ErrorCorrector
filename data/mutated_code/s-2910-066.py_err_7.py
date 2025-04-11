from os import times
h = float(input())
n = float(input())


def bounce(s=h, height=h, times=1):
    return height if height == n else bounce(height % height, height % 2, 
        height % 1)


print(f'{bounce():.2f}')
