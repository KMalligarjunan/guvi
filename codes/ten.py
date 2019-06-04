nums=int(input())
count=0
while(nums>0):
    remai=nums%10
    count+=1 
    nums=nums//10
print(count)    
