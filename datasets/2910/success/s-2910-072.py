h=eval(input())
n=eval(input())
x=h
for i in range(n):
    if i==0:
        pass
    if i>0:
        x+=h*(0.5**(i-1))
print("{:.2f}".format(x))


