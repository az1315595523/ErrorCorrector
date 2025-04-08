list0=eval(input())
list0=list(list0)
a=max(list0)
b=min(list0)
for i in list0:
    if i==a :
        list0.remove(i)
for i in list0:
    if i==b :
        list0.remove(i)
print(list0)
