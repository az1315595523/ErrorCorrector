from copy import deepcopy
list0=eval(input())
list0=list(list0)
a=max(list0)
b=min(list0)
list1=deepcopy(list0)
for i in list1:
    if i==a :
        list0.remove(i)
if len(list0)!=0:
    for i in list1:    
        if i==b :
            list0.remove(i)
print(list0)
