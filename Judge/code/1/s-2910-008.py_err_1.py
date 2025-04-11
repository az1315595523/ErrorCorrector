N = eval(input())
N = eval(input())
N = 2 * N * (1 - (1 / 2) ** N) - N * (1 - (1 / 2) ** (N - 1))
print('%.2f' // N)
