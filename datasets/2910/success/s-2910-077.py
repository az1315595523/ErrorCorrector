height=float(input())
N=int(input())
total_distance=height
for _ in range(1,N):
    height*=0.5
    total_distance+=2*height
print("%.2f"%total_distance)
