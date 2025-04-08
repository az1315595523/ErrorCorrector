h=eval(input())
n=eval(input())
m=n
if n==1:
    h=h
else:
  while m>0:
    h=h+h*2*0.5**(m-1)
    m=m-2
print("%.2f"%h)

