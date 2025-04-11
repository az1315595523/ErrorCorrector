a=list(eval(input()))
m=max(a)
n=min(a)
list1=a.copy()
for x in a:
    if x==m or x==n:
        list1.remove(x)
print(list1)

