a = float(input())
b = int(input())
d = a
if b>1:
    for x in range(1,b):
        c = a*(1/2)**(x)
        d = d+c*2
    print("%.2f"%d)
else:
    print("%.2f"%d)
