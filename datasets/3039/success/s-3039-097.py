lst = eval(input())
m = max(lst)
n = min(lst)
for i in range(lst.count(m)):
    lst.remove(m)
for i in range(lst.count(n)):
    lst.remove(n)
print(lst)
