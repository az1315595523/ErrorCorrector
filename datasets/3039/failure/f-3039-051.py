list1=eval(input())
m=max(list1)
n=min(list1)
for x in list1:
    if x==m or x==n:
        list1.remove(x)
print(list1)
