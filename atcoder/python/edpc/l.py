n=int(input())
a=list(map(int,input().split()))
dp=[[-10**18]*n for i in range(n)]
for i in range(n):
    dp[i][i]=a[i]
for dx in range(2,n+1):
    for l in range(n):
        r=l+dx-1
        if not 0<=l<=r<n:
            continue
        if 0<=l+1<n:
            dp[l][r]=max(dp[l][r],a[l]-dp[l+1][r])
        if 0<=r-1<n:
            dp[l][r]=max(dp[l][r],a[r]-dp[l][r-1])
print(dp[0][n-1])