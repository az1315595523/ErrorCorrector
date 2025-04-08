ls=eval(input())
x=max(ls)
y=min(ls)
ls1=[]
for i in range(len(ls)):
    if ls[i]!=x and ls[i]!=y:
        ls1.append(ls[i])
print(ls1)


    
