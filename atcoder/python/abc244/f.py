n,m=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
d=[[-1]*(1<<n) for i in range(n)]
d[0][0]=0
q=[]
for i in range(n):
    d[i][1<<i]=1
    q.append((i,1<<i,1))
for u,j,dd in q:
    for v in g[u]:
        if d[v][j^(1<<v)]!=-1:
            continue
        d[v][j^(1<<v)]=dd+1
        q.append((v,j^(1<<v),dd+1))
ans=0
for i in range(1<<n):
    t=1<<30
    for u in range(n):
        t=min(t,d[u][i])
    ans+=t
print(ans)