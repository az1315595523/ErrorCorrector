nums=eval(input())
max_num=max(nums)
min_num=min(nums)
tmp=nums.copy()
for num in nums:
    if num == max_num or num==min_num:   
        tmp.remove(num) 
print(nums)                                      
                                                                                        
