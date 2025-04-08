h=int(input())
n=int(input())
sums=h
for x in range(n-1):
    sums+=h*(0.5)**(x)
print("%.2f"%(sums))
