h=eval(input())
n=eval(input())
H=h
for i in range(n-1):
    H+=h*0.5**(i)
print("%.2f"%H)

