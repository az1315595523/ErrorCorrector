ls=eval(input())
maxnum=max(ls)
minnum=min(ls)
a=[maxnum,minnum]
ls1=[]
for i in ls:
    if i not in a:
        ls1.append(i)
print(ls1)
