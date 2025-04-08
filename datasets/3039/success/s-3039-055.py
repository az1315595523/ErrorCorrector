lst = eval(input())
G = max(lst)
g = min(lst)
maxnum = lst.count(G)
minmum = lst.count(g)
if G>g:
    for i in range(maxnum):
        lst.remove(G)
    for i in range(minmum):
        lst.remove(g)
else:
    for i in range(maxnum):
        lst.remove(G)
print(lst)
