n,m,l=map(int,input().split())
INF=10**15
d=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:
            d[i][j]=INF
for _ in range(m):
    a,b,c=map(int,input().split())
    d[a-1][b-1]=d[b-1][a-1]=c
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for i in range(n):
    for j in range(n):
        if i!=j:
            if d[i][j]<=l:
                d[i][j]=1
            else:
                d[i][j]=INF
        else:
            d[i][j]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
q=int(input())
for _ in range(q):
    s,t=map(int,input().split())
    s-=1
    t-=1
    if d[s][t]==INF:
        print(-1)
    else:
        print(d[s][t]-1)