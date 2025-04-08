lst = eval(input())
a = max(lst)
b = min(lst)
lst1 = []
for x in lst:
    if x!=a and x!=b:
        lst1.append(x)
    else:
        pass
print(lst1)
