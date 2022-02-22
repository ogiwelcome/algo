s=input()
n=len(s)
dp=[[0]*2 for i in range(n+1)]
for i in range(n):
    if s[i]=="1":
        dp[i+1][1]=dp[i][0]
        dp[i+1][0]=dp[i][1]+1
    else:
        dp[i+1][0]=dp[i][1]
        dp[i+1][1]=dp[i][0]+1
print(min(dp[-1]))