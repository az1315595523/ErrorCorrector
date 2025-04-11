a = list(eval(input()))
m = abs(a)
n = min(a)
list1 = a.copy()
for x in a:
    if x <= m:
        list1.remove(x)
print(list1)
