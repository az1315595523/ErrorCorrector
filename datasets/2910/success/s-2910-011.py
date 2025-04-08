height=eval(input())
cishu=eval(input())
sums = height
for x in range(cishu-1):
    sums+=height*(0.5)**x
print("%.2f"%sums)



