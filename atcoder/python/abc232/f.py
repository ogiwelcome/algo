n,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
INF=10**18
dp=[INF]*(1<<n)
dp[0]=0
for i in range(1<<n):
    cnt=0
    for j in range(n):
        if (i>>j)&1:
            cnt+=1
    for k in range(n):
        if (i>>k)&1:continue
        cnt2=0
        for l in range(k):
            if (i>>l)&1==0:
                cnt2+=1
        dp[i^(1<<k)]=min(dp[i^(1<<k)],dp[i]+abs(a[k]-b[cnt])*x+cnt2*y)
print(dp[-1])