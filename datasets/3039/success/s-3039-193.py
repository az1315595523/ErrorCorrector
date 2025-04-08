a=eval(input())
max=max(a)
min=min(a)
for x in reversed(a):
    if x==max or x==min:
        a.remove(x)
print(a)
