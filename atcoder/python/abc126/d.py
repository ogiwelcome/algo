n=int(input())
g=[[] for i in range(n)]
for _ in range(n-1):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    g[u].append([v,w])
    g[v].append([u,w])
d=[0]*n
q=[[-1,0]]
while q:
    par,v=q.pop()
    for to,w in g[v]:
        if par==to:
            continue
        d[to]=d[v]+w
        q.append([v,to])
c=[d[i]%2 for i in range(n)]
print(*c,sep="\n")