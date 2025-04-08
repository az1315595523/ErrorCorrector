h = eval(input())
N = eval(input())
s = h
l = 0
for i in range(1,N+1):
    s = s + 2 * l
    l = h*(0.5**i)
print("%.2f"%(s))
