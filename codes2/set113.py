a=int(input())
s=input().split()
l=[]
for i in range(0,len(s)):
    l.append(s[i].lower())
a=sorted(l)
for i in range(0,len(a)):
    print(a[i])
