n=int(input())
s=input().split()
st=""
for i in range(0,len(s)):
	if(int(s[i])==i):
		st+=s[i]+" "
		print(s[i],end=" ")
if(st==""):
	print(-1)
