lst=eval(input())
a=max(lst)
b=min(lst) 
lst1=lst.copy()
for i in lst:
    if i==a or i==b:
        lst1.remove(i)
print(lst1)
