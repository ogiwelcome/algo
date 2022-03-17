import sys
sys.setrecursionlimit(10**6)
n,k=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
mod=10**9+7
def dfs(v, par, rest):
    used=1
    if v>0:
        used+=1
    res = rest
    for to in g[v]:
        if to!=par:
            res*=dfs(to,v,k-used)
            res%=mod
            used+=1
    return res
print(dfs(0,-1,k))