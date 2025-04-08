lst = eval(input())
a = max(lst)
b = min(lst)
lst = [x for x in lst if x!= a and x != b]
   

print(lst)
