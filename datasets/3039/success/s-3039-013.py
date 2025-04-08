n=eval(input())
a=max(n)
b=min(n)
while a in n:
    n.remove(a)
while b in n:
    n.remove(b)
print(n)
