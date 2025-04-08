h=eval(input())
n=eval(input())
a=h
list1=[]
for i in range(1,n):
    a=a/2
    s=2*a
    list1.append(s)
list1.append(h)
lc=sum(list1)
print("%.2f"%(lc))
