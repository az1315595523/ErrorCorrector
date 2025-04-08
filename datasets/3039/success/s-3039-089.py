a = eval(input())
max_value = max(a)
min_value = min(a)
while(max_value in a):
    a.remove(max(a))
while(min_value in a):
    a.remove(min(a))
print(a)
