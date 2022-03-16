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

n,m=map(int,input().split())
edges=[list(map(int,input().split())) for i in range(m)]
uf=UnionFind(n)
flg=True
cnt_in=[0]*n
for u,v in edges:
    u-=1
    v-=1
    if uf.same(u,v):
        flg=False
    uf.union(u,v)
    cnt_in[u]+=1
    cnt_in[v]+=1
if not flg:
    print("No")
    exit()
if max(cnt_in)>=3:
    print("No")
else:
    print("Yes")