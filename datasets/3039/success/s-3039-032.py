list1 = eval(input())
list2 = sorted(list1)
while len(list1) > 0 and max(list1) == max(list2):
    list1.remove(max(list1))
while len(list1) > 0 and min(list1) == min(list2):
    list1.remove(min(list1))
print(list1)
