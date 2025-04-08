a=eval(input())
a=list(a)
b=max(a)
c=min(a)
list2=[]

for x in a:
    if x!=b and x!=c:
        list2.append(x)

print(list2)



