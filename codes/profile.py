n=int(input())
s=input().split()
for i in range(0,len(s)):
	if(s.count(s[i])==1):
		print(int(s[i]))
