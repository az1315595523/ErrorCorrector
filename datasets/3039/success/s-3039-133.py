lst=eval(input())
lst1=lst.copy()
maxl=max(lst)
minl=min(lst)
for i in lst1:
    if i==maxl or i==minl:
        lst.remove(i)
print(lst)
