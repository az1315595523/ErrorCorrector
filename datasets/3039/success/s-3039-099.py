list1 = eval(input())
list1 = list(list1)
a = max(list1)
b = min(list1)
count1 = 0
count2 = 0
for x in list1:
    if x == a or x == b:
        list1[count2] = '#'
        count1 += 1
    count2 += 1
while count1 > 0:
    list1.remove('#')   # 原来一次只删除一个'#'啊
    count1 -= 1
print(list1)
