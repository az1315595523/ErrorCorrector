a=eval(input())
b=eval(input())
c=a
for i in range(b-1):
    x=(0.5)**i
    d=a*x
    c+=d
print("%.2f"%c)
