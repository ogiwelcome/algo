l=list(input())
n=len(l)
mod=10**9+7
# 桁dp、0->未確定/1->確定
dp=[[0]*2 for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    if l[i]=="1":
        # (0,0)
        dp[i+1][1]+=dp[i][0]+dp[i][1]
    else:
        # (0,0)
        dp[i+1][1]+=dp[i][1]
        dp[i+1][0]+=dp[i][0]
    # (1,0),(0,1)
    if l[i]=="1":
        dp[i+1][1]+=dp[i][1]*2
        dp[i+1][0]+=dp[i][0]*2
    else:
        dp[i+1][1]+=dp[i][1]*2
    dp[i+1][0]%=mod
    dp[i+1][1]%=mod
print(sum(dp[n])%mod)