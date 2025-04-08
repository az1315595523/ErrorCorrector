a = eval(input())
c =max(a)
b = min(a)
if b ==c:
    print("[]")
else:

    
    d = a.count(c)
    e = a.count(b)
    for i in range(1,d+1):
        a.remove(c)
    for i in range(1,e+1):
        a.remove(b)
    print(a)

