n,u,v=map(int,input().split())
u-=1
v-=1
g=[[] for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
du=[0]*n
q=[[-1,u]]
while q:
    par,ver=q.pop()
    for to in g[ver]:
        if par==to:
            continue
        du[to]=du[ver]+1
        q.append([ver,to])
dv=[0]*n
q=[[-1,v]]
while q:
    par,ver=q.pop()
    for to in g[ver]:
        if par==to:
            continue
        dv[to]=dv[ver]+1
        q.append([ver,to])
ans=0
for i in range(n):
    if du[i]<dv[i]:
        ans=max(ans,dv[i])
print(ans-1)