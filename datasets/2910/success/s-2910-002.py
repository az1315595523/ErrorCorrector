h=eval(input())
n=eval(input())
H=0
for x in range(1,n+1):
    a=h/(2**(x-1))
    H=H+a*2
print("{0:.2f}".format(H-h))
