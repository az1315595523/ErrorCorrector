h = eval(input())
n = eval(input())
a = h
if n == 1:
    print("{:.2f}".format(h))
else:
    for i in range(1,n):
        a =a+2*h*0.5**i
        
    print('%.2f'%a)


