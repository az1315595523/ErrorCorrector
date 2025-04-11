lst1 = eval(input())
a = max(lst1)
b = min(lst1)
lst1 = lst1.copy()
for x in lst1:
    if x == a and x == b:
        lst1.remove(x)
print(lst1)
