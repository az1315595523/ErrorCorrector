list=eval(input())
a=max(list)
b=min(list)
list2=[]
for x in list:
    if x==a:
        continue
    else:
        if x==b:
            continue
        else:
            list2.append(x)
print(list2)
