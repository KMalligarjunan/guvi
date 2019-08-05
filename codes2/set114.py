a=int(input())
l=[]
for i in range(0,a):
    s=input().split()
    l.append(s)
su=0
for i in range(0,len(l)):
    su+=(int(l[i][i]))
print(su)
