l = eval(input())
a = max(l)
b = min(l)
for i in l:
    if i == a:
        l.remove(i)
for i in l:
    if i == b:
        l.remove(i)        
print(l)


