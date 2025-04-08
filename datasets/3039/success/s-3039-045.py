list1=eval(input())
m=max(list1)
n=min(list1)
list2=list1.copy()
for x in list1:
    if x==m or x==n:
        list2.remove(x)
print(list2)
