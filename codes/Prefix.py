n=int(input())
l=[]
for i in range(0,n):
	s=input()
	l.append(s)
k=[]
for i in range(0,n):
	k.append(len(l[i]))
a=min(k)
k=l[0]
l.remove(l[0])
b=""
for i in range(0,a):
	count=0
	for j in range(0,len(l)):
		if(k[i]==l[j][i]):
			count+=1
	if(count==len(l)):
		b=b+k[i]
	else:
		break
print(b)
