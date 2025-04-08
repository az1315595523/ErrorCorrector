t=eval(input())
t.sort()
a=t[0]
b=t[-1]
for i in t:
    if i==a:
        t=t[1:]
    elif i==b:
        t=t[:-1]
print(t)
