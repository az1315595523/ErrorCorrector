h = float(input())
n = int(input())
kong = [h]
if n==1:
    print(h)
else:
    for i in range(n-1):
        h = h*0.5
        kong.append(h*2)
print("%.2f"%(sum(kong)))
