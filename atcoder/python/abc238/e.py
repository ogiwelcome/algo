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

n,q=map(int,input().split())
lr=[list(map(int,input().split())) for i in range(q)]
uf=UnionFind(n+1)
for l,r in lr:
    uf.union(l-1,r)
if uf.same(0,n):
    print("Yes")
else:
    print("No")