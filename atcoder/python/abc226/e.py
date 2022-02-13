n,m=map(int,input().split())
mod=998244353
g=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)
vis=[False]*n
ans=1
for i in range(n):
    if vis[i]:
        continue
    q=[i]
    cnt_v=0
    edges=set()
    while q:
        v=q.pop()
        if vis[v]:
            continue
        vis[v]=True
        cnt_v+=1
        for to in g[v]:
            if not vis[to]:
                q.append(to)
                edges.add((min(v,to),max(v,to)))
    cnt_e=len(edges)
    if cnt_e==cnt_v:
        ans*=2
        ans%=mod
    else:
        ans=0
print(ans)