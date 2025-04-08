h = eval(input())
N = eval(input())
l = h
for i in range(N-1):
    h = 0.5*h
    b = 2*h
    l += b
print("%.2f"%l)    
