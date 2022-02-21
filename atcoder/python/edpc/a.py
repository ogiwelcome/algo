n=int(input())
h=list(map(int,input().split()))
dp=[0]*(n+1)
dp[2]=abs(h[1]-h[0])
for i in range(2,n):
    dp[i+1]=min(dp[i]+abs(h[i]-h[i-1]),dp[i-1]+abs(h[i]-h[i-2]))
print(dp[n])