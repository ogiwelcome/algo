n,W=map(int,input().split())
INF=10**18
wv=[list(map(int,input().split())) for i in range(n)]
V=10**5
dp=[[INF]*(V+1) for i in range(n+1)]
# dp_i_j: i番目まで見て価値をjにするような最小のw
for i in range(n+1):
    dp[i][0]=0
for i in range(n):
    w,v=wv[i]
    for j in range(V+1):
        if j-v>=0:
            dp[i+1][j]=min(dp[i][j],dp[i][j-v]+w)
        else:
            dp[i+1][j]=dp[i][j]
ans=0
for i in range(V+1):
    if dp[-1][i]<=W:
        ans=i
print(ans)