n,m=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
# dp_i: iからスタートする場合の最長路の長さ

def dfs(v):
    ans=0
    for to in g[v]:
        if dp[to]==0:
            dfs(to)
        ans=max(ans,dp[to])
    dp[v]=ans+1

dp=[0]*n
vis=[False]*n
for i in range(n):
    dfs(i)
print(max(dp)-1)