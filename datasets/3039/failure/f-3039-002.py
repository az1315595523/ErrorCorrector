a=eval(input())
b=max(a)
c=min(a)
a1=a.copy()
for x in a:
      if x==a or x==b :
        a1.remove(x)
print(a1)

