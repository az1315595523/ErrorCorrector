a=list(eval(input()))
if a.count(max)>1 or a.count(min)>1:
    for i in range(2):
        a.remove(max(a))
        a.remove(min(a))
else:
    a.remove(max(a))
    a.remove(min(a))
print(a)
