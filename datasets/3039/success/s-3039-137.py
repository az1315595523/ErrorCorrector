ls=eval(input())
n,m=max(ls),min(ls)
while n in ls:
    ls.remove(n)
while m in ls:
    ls.remove(m)
print(ls)
