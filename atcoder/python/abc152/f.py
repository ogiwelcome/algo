n=int(input())
g=[[] for i in range(n)]
edges=[list(map(lambda x:int(x)-1,input().split())) for i in range(n-1)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)
m=int(input())
uv=[list(map(lambda x:int(x)-1,input().split())) for i in range(m)]
# n:size
# par:parent
# depth:depth from root
# 0-indexed
bit_l = (n-1).bit_length()


def construct(par):
    par_k = [par]
    s = par
    for k in range(bit_l):
        ss = [-1]*n
        for i in range(n):
            if s[i] < 0:
                continue
            ss[i] = s[s[i]]
        par_k.append(ss)
        s = ss
    return par_k


def lca(u, v, par_k, depth):
    dd = depth[v]-depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd
    for k in range(bit_l+1):
        if dd & 1:
            v = par_k[k][v]
        dd >>= 1
    if u == v:
        return u
    for k in range(bit_l-1, -1, -1):
        pu = par_k[k][u]
        pv = par_k[k][v]
        if pu != pv:
            u = pu
            v = pv
    return par_k[0][u]

q=[0]
depth=[0]*n
par=[-1]*n
while q:
    v=q.pop()
    for to in g[v]:
        if par[to]==-1:
            par[to]=v
            depth[to]=depth[v]+1
            q.append(to)
par_k=construct(par)
lca_arr=[[lca(i,j,par_k,depth) for j in range(n)] for i in range(n)]
edge_idx={}
idx=0
for u,v in edges:
    if u>v:
        u,v=v,u
    edge_idx[(u,v)]=idx
    idx+=1
ss=[set() for i in range(m)]
for i in range(m):
    u,v=uv[i]
    p=lca_arr[u][v]
    while u!=p:
        tmp=u
        u=par[u]
        ss[i].add(edge_idx[(min(tmp,u),max(tmp,u))])
    while v!=p:
        tmp=v
        v=par[v]
        ss[i].add(edge_idx[(min(tmp,v),max(tmp,v))])
ans=0
p2=[1<<i for i in range(61)]
for i in range(1,2**m):
    use=set()
    cnt=0
    for j in range(m):
        if (i>>j)&1:
            use|=ss[j]
            cnt+=1
    l=len(use)
    if cnt%2:
        ans+=p2[n-1-l]
    else:
        ans-=p2[n-1-l]
print(2**(n-1)-ans)