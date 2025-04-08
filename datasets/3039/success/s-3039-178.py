a = eval(input())
b = a.copy()
m=max(a)
n=min(a)
for i in b:
    if i == m or i== n:
        a.remove(i)
print(a)
