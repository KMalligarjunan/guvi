n1,n2=input().split()
n1,n2=int(n1),int(n2)
for i in range(n1+1,n2):
	temp=1
	for j in range(2,i):
		if(i%j==0):
			temp=0
			break
	if(temp==1):
		print(i,end=" ")
