n,m,p=map(int,input().split())
edges=[]
for rep in range(m):
    u,v,c=map(int,input().split())
    edges.append([u-1,v-1,p-c])
INF=float("inf")
d=[INF]*n
d[0]=0
for i in range(2*n):
    for u,v,c in edges:
        if d[v]>d[u]+c:
            d[v]=d[u]+c
            if i>=n:
                d[v]-=INF
    if i==n-1:
        ans=d[-1]
if ans!=d[-1]:
    print(-1)
else:
    print(max(0,-ans))