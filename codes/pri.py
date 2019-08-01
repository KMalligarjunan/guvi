l,r=input().split()
l,r=int(l),int(r)
temp=0
for Number in range (l,r+1):
    count = 0
    for i in range(2,Number):
        if(Number % i == 0):
            count = count + 1
            break
    if (count == 0 and Number != 1):
        temp+=1
print(temp)
