h,w=map(int,input().split())
c=[list(input()) for i in range(h)]
dp=[[0]*w for i in range(h)]
dp[0][0]=1
INF=10**9
for i in range(1,h):
    if c[i][0]==".":
        dp[i][0]=dp[i-1][0]+1
    else:
        dp[i][0]=-INF
for j in range(1,w):
    if c[0][j]==".":
        dp[0][j]=dp[0][j-1]+1
    else:
        dp[0][j]=-INF
for i in range(1,h):
    for j in range(1,w):
        if c[i][j]==".":
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])+1
        else:
            dp[i][j]=-INF
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,dp[i][j])
print(ans)