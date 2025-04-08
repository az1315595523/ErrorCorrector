a = eval(input())
for i in a:
   if i >= max(a) or i <= min(a):
      a.remove(i)
print(a)

