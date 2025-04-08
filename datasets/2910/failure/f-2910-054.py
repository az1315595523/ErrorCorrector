from cgi import print_environ


h=eval(input())
N=eval(input())
s=0
for x in range(1,N+1):
          H=h/2
          s=s+H*2
print("%.2f"%s)
