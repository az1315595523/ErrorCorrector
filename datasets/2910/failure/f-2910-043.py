h=eval(input())
n=eval(input()) 
total=h 
for x in range(n-1):
    total+=total*(0.5**x)




print(format(total,'.2f'))


