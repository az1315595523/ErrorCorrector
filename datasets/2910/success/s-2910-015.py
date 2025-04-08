
h = eval(input())
n = eval(input())
if n==1:
    l=h
elif n==2:
    l=h*2
else:
    l=h*2
    for i in range(1,n-1):
        h = h*0.5
        l+=h
print("%.2f"%l)
