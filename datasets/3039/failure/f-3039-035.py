l = eval(input())
a = max(l)
b = min(l)
l2=[]
for i in l:
    if i == a:
        continue
    else:
        l2.append(i)
for i in l:
    if i == b:
        continue
    else:
        l2.append(i)        
print(l)


