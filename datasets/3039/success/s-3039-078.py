lst=eval(input())
lst1=lst.copy()
for x in lst:
    if x==max(lst) or x==min(lst):
        lst1.remove(x)
print(lst1)
