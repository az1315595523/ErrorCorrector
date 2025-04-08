n1=eval(input())
n2=0
n3=max(n1)
for x in n1:
    if x>=n2:
        n2=x
n1.remove(n2)
for y in n1:
    if y<=n3:
        n3=y
n1.remove(n3)
print(n1)

