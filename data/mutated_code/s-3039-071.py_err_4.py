m = list(eval(input()))
m = max(m)
n = min(m)
list1 = m.copy()
for x in m:
    if x == m:
        list1.remove(x)
print(list1)
