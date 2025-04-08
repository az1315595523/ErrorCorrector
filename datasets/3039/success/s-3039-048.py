ls1 = eval(input())
a = max(ls1)
b = min(ls1)
if a == b:
    print("[]")
else:
    while a in ls1:
        ls1.remove(a)
    while b in ls1:
        ls1.remove(b)
    print(ls1)
       
    


