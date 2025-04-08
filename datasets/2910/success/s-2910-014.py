h = eval(input())
n = eval(input())
if n ==1:
    l = h
elif n ==2:
    l =2*h
else:
    l =2*h
    for i in range(1,n-1):
        h = h*0.5
        l = l+h
print('%.2f'%l)

        
        
    
                    
                    
                
        


    
                


