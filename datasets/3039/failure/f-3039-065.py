a=list(eval(input()))
max_num=max(a)
min_num=min(a)
for i in a:
    if i==max_num or i==min_num:
        a.remove(i)
print(a)
