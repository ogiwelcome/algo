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

n,m,k=map(int,input().split())
uf=UnionFind(n)
cnt=[0]*n
for _ in range(m):
    u,v=map(int,input().split())
    uf.union(u-1,v-1)
    cnt[u-1]+=1
    cnt[v-1]+=1
for _ in range(k):
    u,v=map(int,input().split())
    if uf.same(u-1,v-1):
        cnt[u-1]+=1
        cnt[v-1]+=1
ans=[]
for i in range(n):
    ans.append(uf.size(i)-cnt[i]-1)
print(*ans)