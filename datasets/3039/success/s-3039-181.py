ls = eval(input())
ma = max(ls)
mi = min(ls)
ls1 = ls.copy()
for num in ls1:
    if num == ma or num == mi:
        ls.remove(num)
print(ls)
