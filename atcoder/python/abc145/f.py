n,k=map(int,input().split())
h=[0]+list(map(int,input().split()))
dp=[[10**18]*(n+1) for i in range(n+1)]
dp[0][0]=0
for x in range(n):
    for y in range(n-k):
        for l in range(1,x+2):
            dp[x+1][y+1]=min(dp[x+1][y+1],dp[x+1-l][y]+max(0,h[x+1]-h[x+1-l]))
ans=10**18
for i in range(n+1):
    ans=min(ans,dp[i][n-k])
print(ans)