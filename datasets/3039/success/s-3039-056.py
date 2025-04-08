ls=eval(input())
ma=max(ls)
mi=min(ls)
num=0
for i in range(len(ls)):
    for x in ls:
        if x==ma or x==mi:
            ls.remove(x)
print(ls)
