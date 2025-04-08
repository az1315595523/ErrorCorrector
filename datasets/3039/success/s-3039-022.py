ls1=eval(input())
ls2=[]
a=max(ls1)
b=min(ls1)
for i in ls1:
    if i!=a and i!=b:
        ls2.append(i)
print(ls2)

