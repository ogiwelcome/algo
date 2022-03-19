n,k=map(int,input().split())
a=list(map(int,input().split()))
yakusu=set()
s=sum(a)
for i in range(1,int(s**0.5)+1):
    if s%i==0:
        yakusu.add(i)
        yakusu.add(s//i)
ans=1
for d in yakusu:
    r=[a[i]%d for i in range(n)]
    r.sort()
    sr=[r[i] for i in range(n)]
    for i in range(n-1):
        sr[i+1]+=sr[i]
    for i in range(n):
        if sr[i]+sr[n-1]-sr[i]==d*(n-1-i) and sr[i]<=k:
            ans=max(ans,d)
            break
print(ans)