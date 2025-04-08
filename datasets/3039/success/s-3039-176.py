from ast import Del


list=eval(input())
a=max(list)
b=min(list)
list1=[]
for x in list:
    if x!=a and x!=b:
       list1.append(x)
print(list1) 

