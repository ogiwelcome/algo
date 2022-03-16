n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[10**9]*(n+1)
dp[0]=dp[1]=0
for i in range(1,n+1):
    for j in range(1,k+1):
        if i-j>=1:
            dp[i]=min(dp[i],dp[i-j]+abs(h[i-1]-h[i-j-1]))
print(dp[n])