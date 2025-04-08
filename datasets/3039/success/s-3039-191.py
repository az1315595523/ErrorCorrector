list1=eval(input())
a=list1.count(max(list1))
b=list1.count(min(list1))
if len(list1)>0:
    for x in range(a):
        del list1[list1.index(max(list1))]
if len(list1)>0:
    for x in range(b):
        del list1[list1.index(min(list1))]
print(list1)
