


h=eval(input())
n=eval(input())
t=2
x=0
s=h
for i in range(n-1):
    s=s+(h/(t**x))
    x=x+1
print ("%.2f"%s)


