lst=eval(input())
lst2=[]
a=max(lst)
b=min(lst)
for i in lst:
    if i!=a and i!=b:
        lst2.append(i)
print(lst2)
