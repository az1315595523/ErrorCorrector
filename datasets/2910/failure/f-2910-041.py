h=eval(input())
n=eval(input()) 
total=h 
for x in range(n):
    total=total+total*0.5**n
print(format(total,'.2f'))


