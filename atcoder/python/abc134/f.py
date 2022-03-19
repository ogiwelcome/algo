n,k = map(int,input().split())
mod=10**9+7
dp=[[[0]*(n*n+1) for i in range(n+1)] for j in range(n+1)]
dp[0][0][0]=1
for i in range(1,n+1):
    for j in range(n+1):
        for l in range(n*n+1):
            if l-2*j>=0:
                dp[i][j][l]+=(2*j+1)*dp[i-1][j][l-2*j]
            if j+1<=n:
                dp[i][j][l]+=(j+1)*(j+1)*dp[i-1][j+1][l-2*j]
            if j-1>=0:
                dp[i][j][l]+=dp[i-1][j-1][l-2*j]
            dp[i][j][l]%=mod
print(dp[n][0][k])