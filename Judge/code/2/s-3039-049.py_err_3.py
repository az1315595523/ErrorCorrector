jishu1 = eval(input())
jishu1 = list(jishu1)
jishu1 = max(jishu1)
b = min(jishu1)
jishu1 = 0
jishu2 = 0
for x in jishu1;
    if x == b:
        jishu1[jishu2] = 'c'
        jishu1 += 1
    jishu2 += 1
while jishu1 > 0:
    jishu1.remove('c')
    jishu1 -= 1
print(jishu1)