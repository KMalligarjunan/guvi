n=int(input())
sum=0
while(n>0):
    t=n%10
    sum+=(t*t)
    n=n//10
print(sum)
