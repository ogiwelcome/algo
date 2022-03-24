n=int(input())
g=[[] for i in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
mod=10**9+7
q=[[-1,0]]
p=[-1]*n
order=[]
while q:
    par,ver=q.pop()
    order.append(ver)
    for to in g[ver]:
        if to!=par:
            q.append([ver,to])
            p[to]=ver
order.reverse()
c=[1]*n
for v in order:
    if v==0:continue
    c[p[v]]+=c[v]
f2=[0]*(n+1)
f2[0]=1
for i in range(1,n+1):
    f2[i]+=f2[i-1]*2%mod
ans=[0]*n
for i,l in enumerate(g):
    ci=c[i]
    if len(l)>1:
        sc=0
        for to in l:
          cj=c[to]
          sc+=(f2[cj] if cj<ci else f2[n-ci])-1
          ans[i]=(f2[n-1]-sc-1)%mod
print(sum(ans)*pow(f2[n],mod-2,mod)%mod)