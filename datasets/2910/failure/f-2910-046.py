
x=list(input())
for i in range(len(x)):
    x[i]=(int(x[i])+5)%10
x[0],x[1],x[-2],x[-1]=x[-1],x[-2],x[1],x[0]
for i in x:
    print(i,end="")
    


