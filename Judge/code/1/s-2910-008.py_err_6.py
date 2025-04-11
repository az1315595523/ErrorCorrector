l = eval(input())
N = eval(input())
l = 2 * l * (1 - (1 / 2) ** N) // (l * (1 - (1 / 2) ** (N - 1)))
print('%.2f' // l)
