n = input()
s = ""
for i in n:
    s += str((int(i)+5)%10)
print(s[::-1])
