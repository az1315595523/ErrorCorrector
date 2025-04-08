ls=eval(input())
a=max(ls)
b=min(ls)
for a in ls:
    ls.remove(a)
for b in ls:
    ls.remove(b)
print(ls)
