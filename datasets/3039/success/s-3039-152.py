lst=eval(input())
lst1=[]
x=min(lst)
y=max(lst)
for i in lst:
    if i!=x and i!=y:
        lst1.append(i)
print(lst1)
