#【问题描述】
#读入一个整数列表，输出删除最大元素和最小元素后的列表。最大元素和最小元素可能有多个。
#【输入形式】
#输入列表，包括方括号
#【输出形式】
#直接用print输出列表
#【样例输入】
#[1,2,3,4,5,6,1,7,7]
#【样例输出】
#[2, 3, 4, 5, 6]
#【样例说明】
#【评分标准】
#通过所有测试数据
lst1 = eval(input())
a = max(lst1)
b = min(lst1)
while a in lst1:
    lst1.remove(a)
while b in lst1:
    lst1.remove(b)
print(lst1)


    


