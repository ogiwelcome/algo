n=input()
l=len(n)
k=int(input())
dp=[[[0]*(k+1) for i in range(2)] for j in range(l+1)]
dp[0][1][0]=1
for i in range(l):
    for j in range(k+1):
        ni=int(n[i])
        dp[i+1][1][j]+=dp[i][1][j]*(ni==0)
        dp[i+1][0][j]+=dp[i][0][j]+dp[i][1][j]*(ni>0)
        if j<k:
            dp[i+1][1][j+1]+=dp[i][1][j]*(ni>0)
            dp[i+1][0][j+1]+=dp[i][0][j]*9+dp[i][1][j]*max(0,ni-1)
print(dp[l][0][k]+dp[l][1][k])