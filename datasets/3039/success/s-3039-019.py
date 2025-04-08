a=eval(input())
amax=max(a)
amin=min(a)
b=a.copy()
for n in a:
    if n==amax or n==amin:
        b.remove(n)
print(b)
