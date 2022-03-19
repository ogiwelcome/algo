from collections import deque
n,q=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
cnt=[0]*n
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x
dq=deque([[-1,0]])
order=[]
parent=[-1]*n
while dq:
    par,v=dq.popleft()
    order.append(v)
    for to in g[v]:
        if to==par:
            continue
        parent[to]=v
        dq.append([v,to])
for v in order:
    for to in g[v]:
        if to!=parent[v]:
            cnt[to]+=cnt[v]
print(*cnt)