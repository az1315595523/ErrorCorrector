'''a=input().split(',')
a=list(a)
b=eval(input())
m=[]
for x in range(a):
    n=[]
    n.append(a[x])
    n.append(b[x])
    m.append(n)
print(m)'''

'''n,m,l=map(int,input().split(','))
c=[]
for i in range (m):
    d=n+l*i
    c.append(d)
print(c)'''

'''a=eval(input())
n,m=map(int,input().split(','))
if n<=len(a):
    for x in range (n,m):
        b=a.pop(x)
    print(a)
else:
    print('error')'''

'''a=eval(input())
b=[]
for i in a:
    if i >=2:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:
            b.append(i)
print(b)'''

'''a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if b%c==0:
    print('%d'%(b/c))
else:
    print('%.2f'%(d)) '''

'''a=list(map(str,input().split()))
n,m=map(int,input().split())
a[n],a[m]=a[m],a[n]
print(a)'''

a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>0:
    for x in range(b):
        a.remove(max(a))
if len(a)>0:
    for x in range(c):
        a.remove(min(a))
print(a)

