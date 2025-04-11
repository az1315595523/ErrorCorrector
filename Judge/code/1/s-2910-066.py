from os import times


h=float(input())
n=float(input())

def bounce(s = h, height = h, times = 1):
    return s if times ==n else bounce(s + height, height/2, times + 1)

print(f"{bounce():.2f}")
