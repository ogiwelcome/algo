n=int(input())
p=list(map(float,input().split()))
dp=[[0]*(n+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    dp[i+1][0]=dp[i][0]*(1-p[i])
    for j in range(n):
        dp[i+1][j+1]=dp[i][j]*p[i]+dp[i][j+1]*(1-p[i])
ans=0
for j in range((n+1)//2,n+1):
    ans+=dp[n][j]
print(ans)