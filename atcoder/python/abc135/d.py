s=input()
n=len(s)
mod=10**9+7
dp=[[0]*13 for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    if s[i]=="?":
        for j in range(13):
            for k in range(10):
                dp[i+1][(j*10+k)%13]+=dp[i][j]
                dp[i+1][(j*10+k)%13]%=mod
    else:
        x=int(s[i])
        for j in range(13):
            dp[i+1][(10*j+x)%13]+=dp[i][j]
            dp[i+1][(10*j+x)%13]%=mod
print(dp[n][5])