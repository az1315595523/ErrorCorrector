from tkinter import N


h=eval(input())
n=eval(input())
if n==1:
    s=h
else:
    s=h
    for i in range(n-1):
        s += h/(2**i)
print("%.2f"%s)

