h = int(input())
n = int(input())
total_h = h
for i in range(n-1):
    total_h += h*(0.5)**i
print("%.2f"%total_h)
