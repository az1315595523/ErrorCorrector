t=eval(input())
t.sort()
min=t[0]
max=t[-1]
for i in t:
    if i==min:
        t.remove(i)
    elif i==max:
        t.remove(i)
print(t)
