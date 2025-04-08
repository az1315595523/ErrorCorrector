h=eval(input())
N=eval(input())
height=h
for i in range(1,N):
    h=h/2
    height+=h+2
print("%.2f"%(height))
