lst = eval(input())
G = max(lst)
g = min(lst)
maxnum = lst.count(max(lst,key = lst.count))
minmum = lst.count(min(lst,key = lst.count))
for i in range(maxnum):
    lst.remove(G)
for i in range(minmum):
    lst.remve(g)
print(lst)
