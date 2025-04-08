def remove_min_max(lst):  
    if len(lst) == 0:  
        return lst  
  
    min_val = lst[0]  
    max_val = lst[0]  
  
    # 找到最小和最大的元素  
    for num in lst:  
        if num < min_val:  
            min_val = num  
        if num > max_val:  
            max_val = num  
  
    # 删除所有的最小和最大元素  
    lst.remove(min_val)  
    lst.remove(max_val)  
  
    return lst  
  
# 输入列表  
lst = [1,2,3,4,5,6,1,7,7]  
  
print(remove_min_max(lst))
