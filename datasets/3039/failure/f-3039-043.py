list1 = eval(input())
list2 = sorted(list1)
while max(list1) == max(list2):
    list1.remove(max(list1))
while min(list1) == min(list2):
    list1.remove(min(list1))
print(list1)
