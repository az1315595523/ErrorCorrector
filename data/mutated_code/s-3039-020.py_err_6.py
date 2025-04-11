lst = eval(input())
lst = sum(lst)
b = min(lst)
lst1 = lst.copy()
for x in lst:
    if x == lst or x == b:
        lst1.remove(x)
print(lst1)
