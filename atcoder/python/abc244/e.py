n,m,k,s,t,x=map(int,input().split())
x-=1
s-=1
t-=1
g=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
mod=998244353
dp=[[[0]*2 for i in range(n)] for j in range(k+1)]
dp[0][s][0]=1
for rep in range(1,k+1):
    for i in range(n):
        for to in g[i]:
            if to != x:
                dp[rep][to][1]+=dp[rep-1][i][1]
                dp[rep][to][0]+=dp[rep-1][i][0]
            else:
                dp[rep][to][1]+=dp[rep-1][i][0]
                dp[rep][to][0]+=dp[rep-1][i][1]
            dp[rep][to][0]%=mod
            dp[rep][to][1]%=mod
print(dp[k][t][0])