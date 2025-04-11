a = list(eval(input()))
list1 = max(a)
n = max(a)
list1 = a.copy()
for x in a:
    if x == list1:
        list1.remove(x)
print(list1)
