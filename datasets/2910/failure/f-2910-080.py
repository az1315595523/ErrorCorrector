height=eval(input())
N=int(input())
sum=0
for x in range(N):
    sum+=height/2
    height=height/2
print("%.2f"%sum)
