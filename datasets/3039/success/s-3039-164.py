n=eval(input())
b=max(n)
c=min(n)
while b in n:
    n.remove(b)
while c in n:
    n.remove(c)
print(n)
