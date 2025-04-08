list=eval(input())
max=max(list)
min=min(list)
list2=[max,min]
list3=[]
for x in list:
    if x not in list2:
        list3.append(x)
print(list3)
