x=eval(input())
M=max(x)
m=min(x)
while M in x:
    x.remove(M)
while m in x:
    x.remove(m)
print(x)
