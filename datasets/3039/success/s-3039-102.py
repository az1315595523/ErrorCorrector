lst=eval(input())
a=max(lst)
b=min(lst)
for i in lst[:]:
    if i==a or i==b:
        lst.remove(i)
print(lst)
