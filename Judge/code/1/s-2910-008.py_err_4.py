h=eval(input())
N=eval(input())
l=2*h*(1-(1/2)**N)+h*(1-(1/2)**(N-1))
print("%.2f"%l)
