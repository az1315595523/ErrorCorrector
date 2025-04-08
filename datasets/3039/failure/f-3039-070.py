lst = eval(input())
G = max(lst)
g = min(lst)
maxnum = lst.count(max(lst,key = lst.count))
minmum = lst.count(min(lst,key = lst.count))
for i in range(maxnum):
    lst.remove(G)
for i in range(minmum):
    lst.remove(g)[1,2,3,4,5,6,7,8]
print(lst)
