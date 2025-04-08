a = eval(input());d=a.copy()
b=max(a);c=min(a)
for i in d:
    if i==b:
        a.remove(i)
    elif i==c:
        a.remove(i)
    print(a)

