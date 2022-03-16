h,w=map(int,input().split())
a=[list(input()) for i in range(h)]
mod=10**9+7
dp=[[0]*w for i in range(h)]
dp[0][0]=1
for j in range(1,w):
    if a[0][j]==".":
        dp[0][j]+=dp[0][j-1]
for i in range(1,h):
    if a[i][0]==".":
        dp[i][0]+=dp[i-1][0]
for i in range(1,h):
    for j in range(1,w):
        if a[i][j]==".":
            dp[i][j]+=dp[i-1][j]+dp[i][j-1]
            dp[i][j]%=mod
print(dp[-1][-1])