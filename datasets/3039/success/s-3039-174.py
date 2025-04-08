lst=eval(input())
x1=max(lst)
x2=min(lst)
for i in range(lst.count(x1)):
    lst.remove(x1)
for x in range(lst.count(x2)):
    lst.remove(x2)
print(lst)
