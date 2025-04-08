h=eval(input())
n=eval(input())
sum=h
for i in range(n-1):
    sum+=h
    h=h*0.5
print("%.2f"%sum)
      

