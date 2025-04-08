lst=eval(input())

min_number=min(lst)
max_number=max(lst)
len=len(lst)
answer=[]
answer=[lst[i] for i in range(len) if lst[i]!=max_number and lst[i]!=min_number]
#answer=[i for i in lst if i !=max_number and i !=min_number]


print(answer)
