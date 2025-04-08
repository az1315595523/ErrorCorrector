h = float(input())
N = int(input())
H = [h,h*2]
for i in range(1,N-1):
    H.append(int(H[i])+h/(2**i))
print(H[-1])
