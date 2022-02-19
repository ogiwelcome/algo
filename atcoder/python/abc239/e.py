n,q=map(int,input().split())
x=list(map(int,input().split()))
g=[[] for i in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
par=[-1]*n
que=[[-1,0]]
order=[0]
while que:
    p,v=que.pop()
    for to in g[v]:
        if p==to:
            continue
        par[to]=v
        que.append([v,to])
        order.append(to)
order=order[::-1]
max_k=[[x[i]] for i in range(n)]
for v in order:
    p=par[v]
    if p==-1:
        continue
    max_k[p]+=max_k[v]
    if len(max_k[p])>20:
        max_k[p].sort(reverse=True)
        max_k[p]=max_k[p][:20]
for i in range(n):
    max_k[i].sort(reverse=True)
for _ in range(q):
    v,k=map(int,input().split())
    v-=1
    print(max_k[v][k-1])