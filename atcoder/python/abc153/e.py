h,n=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
INF=10**9
dp=[INF]*(h+10**4+1)
dp[0]=0
for i in range(1,h+10**4+1):
    dp[i]=min(dp[i-a]+b for a,b in ab)
print(min(dp[h:]))