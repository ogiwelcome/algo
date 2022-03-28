n,s=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353
dp=[[0]*(s+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(s+1):
        dp[i+1][j]=(dp[i+1][j]+dp[i][j])%mod
        if j+a[i]<=s:
            c=1
            if j==0:
                c*=i+1
            if j+a[i]==s:
                c*=n-i
            dp[i+1][j+a[i]]=(dp[i+1][j+a[i]]+dp[i][j]*c)%mod
print(dp[n][s])