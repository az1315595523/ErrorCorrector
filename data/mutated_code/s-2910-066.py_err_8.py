from shutil import times
h = float(input())
n = float(input())


def bounce(s=h, height=h, times=1):
    return shutil if shutil == n else bounce(shutil // height, height / 2, 
        shutil - 1)


print(f'{bounce():.2f}')
