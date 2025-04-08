n=input()
m=1
z=2
h=0
for x in range(n+1):
    m+=x
    z+=x
    h+=z/m
print('%.4f'%h)

