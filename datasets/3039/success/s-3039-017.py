a=eval(input())
b=max(a)
c=min(a)
while b in a:
    a.remove(b)
while c in a:
    a.remove(c)
print(a)
