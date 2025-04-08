a = eval(input())
c =max(a)
b = min(a)
if b ==c:
    print("[]")
else:

    
    d = a.count(c)
    e = a.count(b)
    for i in range(d):
        a.remove(c)
    for i in range(e):
        a.remove(b)
    print(a)

