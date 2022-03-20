n,m=map(int,input().split())
a=[0]*m
c=[]
for i in range(m):
    aa,bb=map(int,input().split())
    a[i]=aa
    cc=list(map(int,input().split()))
    msk=0
    for ccc in cc:
        ccc-=1
        msk|=(1<<ccc)
    c.append(msk)
INF=10**9
dp=[[INF]*(1<<n) for i in range(m+1)]
dp[0][0]=0
for i in range(m):
    for msk in range(1<<n):
        dp[i+1][msk]=min(dp[i+1][msk],dp[i][msk])
        dp[i+1][msk|c[i]]=min(dp[i+1][msk|c[i]], dp[i][msk]+a[i])
ans=dp[m][(1<<n)-1]
if ans==INF:
    print(-1)
else:
    print(ans)