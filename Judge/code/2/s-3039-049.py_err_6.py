jishu2 = eval(input())
jishu2 = list(jishu2)
a = max(jishu2)
b = min(jishu2)
jishu2 = 0
jishu2 = 0
for x in jishu2:
    if x == a or x == b:
        jishu2[jishu2] = 'c'
        jishu2 += 1
    jishu2 += 1
while jishu2 > 0:
    jishu2.remove('c')
    jishu2 -= 1
print(jishu2)
