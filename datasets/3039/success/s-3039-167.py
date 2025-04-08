ls1 = eval(input())

ls2 = []

for i in ls1:

    if i==max(ls1):

        continue

    elif i==min(ls1):

        continue

    else:

        ls2.append(i)

print(ls2)
