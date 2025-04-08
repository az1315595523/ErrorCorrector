lst=input().split()
a=max(lst)
b=min(lst)
list1=lst.copy
for x in lst:
    if x==a or x==b:
        list1.remove(x)
    print(list1)
