x,y=input().split()
count=0
for i in range(0,len(x)):
    if(x[i]!=y[i]):
        count+=1 
    else:
        continue
if(count==1):
    print("yes")
else:
    print("no")
