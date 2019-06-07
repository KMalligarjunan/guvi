num=int(input())
temp=1
for i in range(2,num):
	if(num%i==0):
		temp=0
		break
if(temp==1):
	print('yes')
else:
	print('no')
