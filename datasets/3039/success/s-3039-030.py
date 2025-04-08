lst = eval(input())
l2 = []
for i in lst:
    if i == max(lst):
        continue
    elif i == min(lst):
        continue
    else:
        l2.append(i)        
print(l2)


