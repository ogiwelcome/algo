n,t=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()
dp=[[0]*(t+3001) for i in range(n+1)]
for i in range(n):
    ai,bi=ab[i]
    for j in range(t):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        dp[i+1][j+ai]=max(dp[i][j+ai],dp[i][j]+bi)
ans=0
for i in range(n+1):
    ans=max(ans,max(dp[i]))
print(ans)