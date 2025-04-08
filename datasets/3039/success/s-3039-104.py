lst=eval(input())
a=max(lst)
b=min(lst)
lst2=lst.copy()
for i in lst:
    if i==a or i==b:
        lst2.remove(i)
print(lst2)
