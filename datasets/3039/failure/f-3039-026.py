a = eval(input())
b = max(a)    
c = min(a)
m = a.count(b)
n = a.count(c)
for i in range(m):
    a.remove(b)
for i in range(n):
    a.remove(c)
print(a)
