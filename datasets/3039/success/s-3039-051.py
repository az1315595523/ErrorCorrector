l=eval(input())
a=max(l)
b=min(l)
for i in range(l.count(a)):
    l.remove(a)
for i in range(l.count(b)):
    l.remove(b)
print(l)
