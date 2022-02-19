from heapq import heappop, heappush
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def all_roots(self):
        roots = set([self.find(i) for i in range(self.n)])
        return list(roots)
    
    def groups(self):
        res = [[] for _ in range(self.n)]
        for i in range(self.n):
            res[self.find(i)].append(i)
        return [group for group in res if group]
n,m=map(int,input().split())
d=list(map(int,input().split()))
if sum(d)!=2*n-2:
    print(-1)
    exit()
uf=UnionFind(n)
deg=[0]*n
for _ in range(m):
    u,v=map(int,input().split())
    deg[u-1]+=1
    deg[v-1]+=1
    uf.union(u-1,v-1)
glps = uf.groups()

mg=[[] for _ in range(len(glps))]
for idx,gp in enumerate(glps):
    for i in gp:
        if d[i]-deg[i]==0:
            continue
        if d[i]-deg[i]<0:
            print(-1)
            exit()
        if d[i]-deg[i]>0:
            for rep in range(d[i]-deg[i]):
                mg[idx].append(i)
mg=sorted(mg,key=len,reverse=True)
me=mg[0]
ans=[]
for other in mg[1::]:
    if not me:
        print(-1)
        exit()
    if not other:
        print(-1)
        exit()
    ans.append([me.pop()+1,other.pop()+1])
    for i in other:
        me.append(i)
if me:
    print(-1)
else:
    for u,v in ans:
        print(u,v)