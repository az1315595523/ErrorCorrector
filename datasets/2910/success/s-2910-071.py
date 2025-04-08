h = int(input())
N = int(input())
n = h
for i in range(N-1):
    h += n
    n = n/2
print("%.2f"%(h))
