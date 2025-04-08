num=eval(input())
max=max(num)
min=min(num)
a=num.copy()
for i in num:
    if i==max or i==min:
        a.remove(i)
print(a)
