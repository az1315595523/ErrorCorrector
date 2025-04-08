ls=eval(input())
ls2=[]
a=max(ls)
b=min(ls)
for i in range(len(ls)):
    if ls[i] != a and ls[i] !=b:
        ls2.append(ls[i])
print(ls2)


