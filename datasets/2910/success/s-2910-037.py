h=eval(input())
n=eval(input())
tot=h
for i in range(n-1):
    tot+=h
    h=h/2
print("%.2f"%tot)
    
