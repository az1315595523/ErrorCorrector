'''s=list(input())
b=[]
for x in s:
    a=str((int(x)+5)%10)
    b.append(a)
b.reverse()
print(''.join(b))'''
h=eval(input())
n=eval(input())
c=[]
for x in range(1,n+1):
    a=h*0.5**x
    b=2*a
    c.append(b)
d=sum(c)
f=h+d
print('%.2f'%(f))

