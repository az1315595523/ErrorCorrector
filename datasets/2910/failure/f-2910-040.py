h = eval(input())
N = eval(input())
s = 0
for x in range(N):
    s = s + h
    h = (1/2)*h
print('{:.2f}'.format(s))
