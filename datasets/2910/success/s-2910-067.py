h=eval(input())
N=eval(input())
lst=[]
a=h
for i in range(N-1):
    a=a*0.5
    lst.append(2*a)
H=sum(lst)+h
print("%.2f"%H)



