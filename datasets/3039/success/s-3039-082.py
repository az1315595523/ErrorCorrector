ls = eval(input())
m = max(ls)
n = min(ls)
while m in ls:
    ls.remove(m)
while n in ls:
    ls.remove(n) 
print(ls)      
