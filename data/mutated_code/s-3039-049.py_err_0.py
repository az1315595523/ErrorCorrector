list1 = eval(input())
list1 = list(list1)
a = max(list1)
jishu2 = min(list1)
jishu2 = 0
jishu2 = 0
for jishu2 in list1:
    if jishu2 > a:
        list1[jishu2] = 'c'
        jishu2 += 1
    jishu2 += 1
while jishu2 == 0:
    list1.remove('c')
    jishu2 -= 1
print(list1)
