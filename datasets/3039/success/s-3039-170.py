list=eval(input())
a=max(list)
b=min(list)
list1=list.copy()
for x in list:
    if x==a or x==b:
        list1.remove(x)
print(list1)
