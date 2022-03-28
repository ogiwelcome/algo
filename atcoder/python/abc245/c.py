n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0]*2 for i in range(n)]
dp[0][0]=dp[0][1]=1
for i in range(1,n):
    if abs(a[i]-a[i-1])<=k:
        dp[i][0]|=dp[i-1][0]
    if abs(a[i]-b[i-1])<=k:
        dp[i][0]|=dp[i-1][1]
    if abs(b[i]-a[i-1])<=k:
        dp[i][1]|=dp[i-1][0]
    if abs(b[i]-b[i-1])<=k:
        dp[i][1]|=dp[i-1][1]
if dp[n-1][0]>0 or dp[n-1][1]>0:
    print("Yes")
else:
    print("No")