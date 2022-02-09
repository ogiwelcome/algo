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
es=[[] for i in range(n)]
for a,b in edges:
    a-=1
    b-=1
    if a>b:
        a,b=b,a
    es[a].append(b)
uf=UnionFind(n)
ans=[]
now=0
for i in range(n)[::-1]:
    now+=1
    for to in es[i]:
        if not uf.same(i,to):
            now-=1
            uf.union(i,to)
    ans.append(now)
ans=ans[::-1]
ans=ans[1:]+[0]
for x in ans:
    print(x)