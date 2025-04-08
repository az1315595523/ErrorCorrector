lst = eval(input())
imax = int(max(lst))
imin = int(min(lst))
nmax = lst.count(imax)
nmin = lst.count(imin)
a = 0
b = 0
if imax != imin:
    while a < nmax:
        lst.remove(imax)
        a += 1
    while b < nmin:
        lst.remove(imin)
        b += 1
    print(lst)
else:
    lst.clear()
    print(lst)

