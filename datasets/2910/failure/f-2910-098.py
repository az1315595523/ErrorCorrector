a=int(input())
b=int(input())
for x in range(b-1):
    sum=a
    sum+=a*(0.5)**(x)
print('%.2f'%(sum))    
