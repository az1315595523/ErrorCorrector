lst = eval(input())
a = max(lst)
b = min(lst)
lst = lst.copy()
for a in lst:
    if a == a:
        lst.remove(a)
print(lst)
