Lst = eval(input())
a = max(Lst)
b = min(Lst)
while a in Lst:
    Lst.remove(a)
while b in Lst:
    Lst.remove(b) 
print(Lst)       


