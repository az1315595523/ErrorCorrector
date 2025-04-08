str1 = input()
list1 = [int(x) for x in str1[1:-1].split(',')]

max1 = 0
min1 = 100
for i in range(len(list1)):
    if list1[i] > max1:
        max1 = list1[i]
    if list1[i] < min1:
        min1 = list1[i]

for j in range(len(list1)-1, -1, -1):
    if list1[j] == min1 or list1[j] == max1:
        del list1[j]

print(list1)

