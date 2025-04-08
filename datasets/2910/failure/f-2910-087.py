h=eval(input())
m=eval(input())
s=0
x=2*h
for i in range(m):
    s=s+x
    x=x*0.5
print('$.2f'%(s-h))
