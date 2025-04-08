h=eval(input())
n=eval(input())
tot=h
for x in range(n-1):
    tot+=h
    h/=2
print("%.2f"%(tot))
