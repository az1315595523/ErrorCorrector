lst=input().split()
a=max(lst)
b=min(lst)
for x in lst:
    if x==a or x==b:
        lst.remove(x)
    print(lst)
