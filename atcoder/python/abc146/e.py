from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    a[i]%=k
sa=[0]+[a[i]-1 for i in range(n)]
for i in range(n):
    sa[i+1]+=sa[i]
    sa[i+1]%=k
dd=defaultdict(int)
j=0
ans=0
for i in range(n+1):
    if i-j==k:
        dd[sa[j]]-=1
        j+=1
    ans+=dd[sa[i]]
    dd[sa[i]]+=1
print(ans)