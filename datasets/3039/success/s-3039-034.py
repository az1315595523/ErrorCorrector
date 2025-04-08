ls=eval(input())
ls2=ls[0:]
ls3=[]
a=max(ls)
b=min(ls)
ls.sort()
for i in range(len(ls)):
    if ls[-1]==a:
        ls.pop()
ls.sort(reverse=True)
for i in range(len(ls)):
    if ls[-1]==b:
        ls.pop()
for i in range(len(ls2)):
    if ls2[i] in ls2 and ls2[i] in ls:
        ls3.append(ls2[i])
print(ls3)
