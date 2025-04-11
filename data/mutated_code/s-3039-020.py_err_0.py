lst = eval(input())
a = max(lst)
b = min(lst)
lst = lst.copy()
for b in lst:
    if b != b:
        lst.remove(b)
print(lst)
