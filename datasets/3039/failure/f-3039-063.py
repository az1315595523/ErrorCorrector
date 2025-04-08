a=list(eval(input()))
for i in range(0,2):
    a.remove(max(a))
    a.remove(min(a))
print(a)
