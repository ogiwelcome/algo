n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
mod=10**9+7
dp=[[0]*(m+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n+1):
    for j in range(m+1):
        if i>0 and j>0 and s[i-1]==t[j-1]:
            dp[i][j]+=dp[i-1][j-1]
        if i>0:
            dp[i][j]+=dp[i-1][j]
        if j>0:
            dp[i][j]+=dp[i][j-1]
        if i>0 and j>0:
            dp[i][j]-=dp[i-1][j-1]
        dp[i][j]%=mod
print(dp[n][m])