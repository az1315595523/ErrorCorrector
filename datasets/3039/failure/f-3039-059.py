ls1 = eval(input())
a = max(ls1)
b = min(ls1)
if a == b:
    while true:
        ls1.remove(a)
        for i in ls1:
            if a not in ls1:
                break
else:
    while true:
        ls1.remove(a)
        for i in ls1:
            if a not in ls1:
                break
while true:
        ls1.remove(b)
        for i in ls1:
            if b not in ls1:
                break
print(ls1)        

    
