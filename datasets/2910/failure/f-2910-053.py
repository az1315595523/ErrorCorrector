h = float(input())
N = int(input())
H = h
if N == 1:
    print("%.2f"%h)
else:
    for i in range(1,N):
        H = H + 2*h*0.5**i
    print("%:.2f"%H)

