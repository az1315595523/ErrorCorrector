h = float(input())
N = int(input())
if N == 1:
    print("%.2f"%h)
else:
    for i in range(N-1):
        h += h
    print("%.2f"%h)
