a=int(input())
l=[]
for i in range(0,a):
    s=input().split()
    l.append(s)
sum=0
for i in range(0,len(l)):
    sum+=(int(l[i][i]))
print(sum)
