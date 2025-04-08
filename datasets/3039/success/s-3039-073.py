list1=eval(input())
list1=list(list1)
a=max(list1)
b=min(list1)
jishu1=0
jishu2=0
for x in list1:
    if x==a or x==b:
        list1[jishu2]='#'
        jishu1+=1
    jishu2+=1
while jishu1>0:
    list1.remove('#')
    jishu1-=1
    print(list1)
