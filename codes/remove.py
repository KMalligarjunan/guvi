from itertools import combinations
n,k=input().split()
n,k=int(n),int(k)
n=list(str(n))
noc=len(n)-k
s=list(combinations(n,noc))
minn=min(s)
num="".join(minn)
num=int(num)
print(num)
