def remove_min_max(lst):  
    if len(lst) == 0:  
        return lst  
  
    min_val = min(lst)  
    max_val = max(lst)  
  
    # 删除所有的最小和最大元素  
    lst = [num for num in lst if num != min_val and num != max_val]  
  
    return lst  
  
# 输入列表  
lst = [1,2,3,4,5,6,1,7,7]  
  
print(remove_min_max(lst))
