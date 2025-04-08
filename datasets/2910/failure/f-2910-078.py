height=eval(input)
N=int(input())
sum=0
for x in range(N+1):
    sum+=height/2
    height=height/2
    print(sum)
