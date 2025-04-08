list1=eval(input())
a=max(list1)
b=min(list1)
list2=list1.copy()
for i in list1:
    if i==a or i==b:
        list2.remove(i)
print(list2)



