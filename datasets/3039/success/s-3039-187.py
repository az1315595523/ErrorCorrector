# lst = eval(input())
# m = max(lst)
# n = min(lst)
# for i in range(lst.count(m)):
#     lst.remove(m)
# for i in range(lst.count(n)):
#     lst.remove(n)
# print(lst)

lst = eval(input())
lst2 = []
m = max(lst)
n = min(lst)
for i in range(len(lst)):
    if lst[i] != m and lst[i] != n:
        lst2.append(lst[i])
print(lst2)
