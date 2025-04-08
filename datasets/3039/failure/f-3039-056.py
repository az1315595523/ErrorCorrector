ls1 = eval(input())
ls2 = []
for i in ls1:
    if i not in ls2:
        ls2.append(i)
else:
    pass
a = max(ls2)
b = min(ls2)
ls2.remove(a)
ls2.remove(b)
print(ls2)        

    
