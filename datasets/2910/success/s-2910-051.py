h = int(input())
n = int(input())
a = h
for x in range(n-1):
    a = a+h
    h = h*0.5
print ("%.2f"%a)
