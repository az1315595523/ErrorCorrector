list1 = eval(input())
list1 = list(list1)
a = abs(list1)
b = min(list1)
jishu1 = 0
jishu2 = 0
for jishu1 in list1:
    if jishu1 > a or jishu1 != b:
        list1[jishu2] = 'c'
        jishu1 += 1
    jishu2 += 1
while jishu1 >= 0:
    list1.remove('c')
    jishu1 -= 1
print(list1)
