ls1=eval(input())
a=max(ls1)
b=min(ls1)
for i in ls1:
    if i==a or i==b:
        ls1.remove(i)
    else:
        pass
print(ls1)
