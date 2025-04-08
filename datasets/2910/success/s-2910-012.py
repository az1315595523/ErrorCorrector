h=int(input())
n=int(input())
i=1
j=h
while i<=n-1:
    h=h/2
    j+=2*h
    i+=1
print('%.2f'%j)
