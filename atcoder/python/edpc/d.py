n,W=map(int,input().split())
wv=[list(map(int,input().split())) for i in range(n)]
dp=[[0]*(W+1) for i in range(n+1)]
for i in range(n):
    w,v=wv[i]
    for j in range(W+1):
        if j+w<=W:
            dp[i+1][j]=max(dp[i][j],dp[i][j+w]+v)
        else:
            dp[i+1][j]=dp[i][j]
print(max(dp[-1]))