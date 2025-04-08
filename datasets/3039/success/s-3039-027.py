a=eval(input())
m=max(a)
n=min(a)
while True:
    if m in a:
        a.remove(m)
    else:
        break
while True:
    if n in a:
        a.remove(n)
    else:
        break
print(a)
