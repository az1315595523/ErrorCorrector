height=eval(input())
N=int(input())
sum=height
for x in range(N-1):
    sum+=height
    height=height/2
print("%.2f"%sum)
