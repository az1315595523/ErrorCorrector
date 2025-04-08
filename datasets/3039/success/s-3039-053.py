a=list(eval(input()))
max_num=max(a)
min_num=min(a)
tmp=a.copy()
for i in a:
    if i==max_num or i==min_num:
        tmp.remove(i)
print(tmp)
