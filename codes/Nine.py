N,K=input().split()
N,K=int(N),int(K)
sum=0
for i in range(1,N+1):
	print(i,end=" ")
for i in range(1,K+1):
	sum+=i
print()
print(sum)
