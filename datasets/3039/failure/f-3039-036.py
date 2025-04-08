from typing import List


lst = eval(input())
a = max(lst)
b = min(lst)
l2=[]
for i in lst:
    if i == a:
        continue
    else:
        l2.append(i)
for i in lst:
    if i == b:
        continue
    else:
        l2.append(i)        
print(l2)


