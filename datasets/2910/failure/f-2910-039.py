h = eval(input())
N = eval(input())
for x in range(N):
    h = h+0.5*h
print('{:.2f}'.format(h))

