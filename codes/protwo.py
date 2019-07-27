N,Q=input().split()
N,Q=int(N),int(Q)
k=input().split()
l=[]
for i in range(0,Q):
    s=input().split()
    l.append(s)
for i in range(0,Q):
    o=[]
    for j in range(int(l[i][0])-1,int(l[i][1])):
        o.append(k[j])
    print(min(o))
