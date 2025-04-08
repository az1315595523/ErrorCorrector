h=eval(input())
N=eval(input())
lst=[h]
for i in range(N-1):
    h=h/2
    lst.append(h)
s=sum(lst)+sum(lst[1:-2])
print("%.2f"%s)
