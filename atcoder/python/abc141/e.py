n=int(input())
s=input()
dp=[[0]*(n+1) for i in range(n+1)]
ans=0
for i in range(n-1,-1,-1):
    for j in range(n-1,i+1,-1):
        if s[i]==s[j]:
            dp[i][j]=max(dp[i][j],dp[i+1][j+1]+1)
            ans=max(ans,min(j-i,dp[i][j]))
print(ans)