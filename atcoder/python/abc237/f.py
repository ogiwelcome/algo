n,m=map(int,input().split())
mod=998244353
dp=[[[[0]*(m+2) for i in range(m+2)] for j in range(m+2)] for k in range(n+1)]
dp[0][m+1][m+1][m+1]=1
for i in range(n):
    for a1 in range(1,m+2):
        for a2 in range(1,m+2):
            for a3 in range(1,m+2):
                for x in range(1,m+1):
                    if x<=a1:
                        dp[i+1][x][a2][a3]+=dp[i][a1][a2][a3]
                    elif x<=a2:
                        dp[i+1][a1][x][a3]+=dp[i][a1][a2][a3]
                    elif x<=a3:
                        dp[i+1][a1][a2][x]+=dp[i][a1][a2][a3]
ans=0
for a1 in range(1,m+1):
    for a2 in range(a1+1,m+1):
        for a3 in range(a2+1,m+1):
            ans+=dp[n][a1][a2][a3]
            ans%=mod
print(ans)