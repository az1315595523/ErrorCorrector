h = eval(input())
n = eval(input())
m = n
if n == 1:
    h = h
else:
    while m > 0:
        h = h + h * 2 * 0.5 ** (m - 1)
        m = m - 1
print("%.2f" % h)

#尝试多次变异，在确定此次变异属于思路错误，算法错误，逻辑错误时，保证语法不会有误，也不会有运行时错误。

# h=eval(input())
# n=eval(input())
# m=n
# total = h
# if n==1:
#     total=h
# else:
#   while m>1:
#     h=h*0.5
#     total+=h*2
#     m=m-1
# print("%.2f"%total)
