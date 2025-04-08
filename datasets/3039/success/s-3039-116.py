ls1=eval(input())
ls2=[]
a=min(ls1)
b=max(ls1)
#print(a,b)
for i in ls1:
    if i!=a and i!=b : ls2.append(i)
print(ls2)
