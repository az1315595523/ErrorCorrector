list_1=eval(input())
a=max(list_1)
min=min(list_1)
nums=list_1.copy()
for i in nums:
   if i==a:
      list_1.remove(i)
   elif i==min:
      list_1.remove(i)
print(list_1)

