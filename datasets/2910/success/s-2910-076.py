h = eval(input())
n = eval(input())
s = h
if n > 1:
    for x in range(n-1):
        h = h/2
        s += h*2
print("%.2f"%s)
