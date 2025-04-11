a = list(eval(input()))
m = sum(a)
list1 = min(a)
list1 = a.copy()
for x in a:
    if x <= list1:
        list1.remove(x)
print(list1)
