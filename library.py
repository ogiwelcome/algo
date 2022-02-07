from collections import defaultdict


class BIT:  # 1-indexed
    def __init__(self, n):
        self.n = n
        self.a = [0]*(n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.a[i] += x
            i += i & -i


############# L C A #################
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
##################################


def z_algorithm(s):
    res = [0]*len(s)
    res[0] = len(s)
    i, j = 1, 0
    while i < len(s):
        while i+j < len(s) and s[j] == s[i+j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < len(s) and k+res[k] < j:
            res[i+k] = res[k]
            k += 1
        i, j = i+k, j-k
    return res
######################SegTree_for_min###################


class SegTree_RMQ():
    def __init__(self, num):
        self.node_size = 1
        while self.node_size < num:
            self.node_size *= 2
        self.INF = 10**18
        self.data = [self.INF]*(2*self.node_size)

    def update(self, k, x):
        k += self.node_size-1
        self.data[k] = x
        while k >= 0:
            k = (k-1)//2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])

    def query(self, l, r):
        nl = l+self.node_size
        nr = r+self.node_size
        res = self.INF
        while nl < nr:
            if nr & 1:
                nr -= 1
                res = min(res, self.data[nr-1])
            if nl & 1:
                res = min(res, self.data[nl-1])
                nl += 1
            nl >>= 1
            nr >>= 1
        return res
###################################


def scc(N, G, RG):
    order = []
    state = [0]*N
    traversed, registered = 1, 2
    for i in range(n):
        if state[i]:
            continue
        stack = [i]
        while stack:
            v = stack[-1]
            if state[v] & registered:
                stack.pop()
                continue
            if not state[v] & traversed:
                state[v] |= traversed
                for to in G[v][::-1]:
                    if not state[to] & traversed:
                        stack.append(to)
            elif not state[v] & registered:
                order.append(stack.pop())
                state[v] |= registered
    order.reverse()
    group = [-1]*n
    label = 0
    for s in order:
        if group[s] >= 0:
            continue
        group[s] = label
        stack = [s]
        while stack:
            v = stack.pop()
            for to in RG[v]:
                if group[to] < 0:
                    stack.append(to)
                    group[to] = label
        label += 1
    return label, group


###### euler tour ########
stack = [[-1, 0, 1]]
in_t = [0]*n
out_t = [0]*n
par = [-1]*n
clock = 0
while stack:
    p, ver, state = stack.pop()
    if state:
        clock += 1
        in_t[ver] = clock
        stack.append([par, ver, 0])
        for to in g[ver]:
            if to != p:
                par[to] = ver
                stack.append([ver, to, 1])
    else:
        out_t[ver] = clock
###########################


def mat_mul(a, b, mod=10**9+7):
    r = [[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])):
                r[i][j] += a[i][k]*b[k][j]
                r[i][j] %= mod
    return r


def mat_pow(a, n):
    r = [[0]*len(a) for i in range(len(a))]
    b = []
    for i in range(len(a)):
        r[i][i] = 1
        b.append(a[i][:])
    l = n
    while l:
        if l & 1:
            r = mat_mul(b, r)
        b = mat_mul(b, b)
        l >>= 1
    return r

################UnionFind###############


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
###############FenwickTree/ BIT###############


class Fenwick():  # 0-indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0]*n

    def cumsum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i-1]
            i -= i & -i
        return res

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.tree[i-1] += x
            i += i & -i

    def query(self, i, j):
        return self.cumsum(j-1)-self.cumsum(i-1)


##########素因数分解(前処理重め)############
N = 2*10**5
nxt = [0 for i in range(N+1)]
for i in range(2, N+1):
    if nxt[i] == 0:
        nxt[i] = i
        for j in range(i*i, N+1, i):
            if nxt[j] == 0:
                nxt[j] = i
############素因数分解カウント(前処理なし・はや)→列挙なら弄る###########


def div(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            while x % i == 0:
                x //= i
                c += 1
    if x > 1:
        c += 1
    return c
##################SparseTable#############################
# 0-indexedで使え


class SparseTable:
    def func(self, a, b):
        return gcd(a, b)

    def __init__(self, arr):
        n = len(arr)
        max_k = (n-1).bit_length()-1
        val = 1  # set by func /ex. min->INF
        table = [[val]*(max_k+1) for i in range(n)]
        for i in range(n):
            table[i][0] = arr[i]
        for k in range(1, max_k+1):
            k2 = 1 << (k-1)
            k3 = 1 << k-1
            for i in range(n-k3):
                table[i][k] = self.func(table[i][k-1], table[k2+i][k-1])
        self.table = table

    def query(self, l, r):  # [l,r)
        d = r-l
        if d == 1:
            return self.table[l][0]
        k = (d-1).bit_length()-1
        k2 = 1 << k
        return self.func(self.table[l][k], self.table[r-k2][k])
# Lagrange補間(係数を返す,mod)


def Lagrange(x, y, mod):
    n = len(x)-1
    for i in range(n+1):
        t = 1
        for j in range(n+1):
            if i != j:
                t *= x[i]-x[j]
                t %= mod
        y[i] *= pow(t, mod-2, mod)
        y[i] %= mod
    p = 0
    q = 1
    dp = [[0]*(n+2) for i in range(2)]
    dp[0][0] = -x[0] % mod
    dp[0][1] = 1
    for i in range(1, n+1):
        for j in range(n+2):
            dp[q][j] = -dp[p][j]*x[i]
            dp[q][j] %= mod
            if j:
                dp[q][j] += dp[p][j-1]
                dp[q][j] %= mod
        p, q = q, p
    res = [0]*(n+1)
    for i in range(n+1):
        if y[i] == 0:
            continue
        if x[i]:
            xinv = pow(x[i], mod-2, mod)
            res[0] -= dp[p][0]*xinv*y[i]
            res[0] %= mod
            prev = -dp[p][0]*xinv % mod
            for j in range(1, n+1):
                res[j] -= (dp[p][j]-prev)*xinv*y[i]
                res[j] %= mod
                prev = -(dp[p][j]-prev)*xinv % mod
        else:
            for j in range(n+1):
                res[j] += dp[p][j+1]*y[i]
                res[j] %= mod
    return res
########### Rolling Hash ################


class RollingHash:
    def __init__(self, string):
        self.n = len(string)
        self.BASE = 1234
        self.MOD = 67280421310721
        self.hash = [0]*(self.n+1)
        self.pow = [1]*(self.n+1)
        for i, char in enumerate(string):
            self.hash[i+1] = (self.hash[i]*self.BASE+ord(char)) % self.MOD
            self.pow[i+1] = (self.pow[i]*self.BASE) % self.MOD

    def get_hash(self, l, r):
        # [l:r]
        res = (self.hash[r]-self.hash[l]*self.pow[r-l]) % self.MOD
        return res
##### mino作るやつ ######
# list(set(minos))とかして


def gen_polyomino(n):
    if n == 1:
        yield ((0, 0),)
        return
    se = set(gen_polyomino(n-1))
    dydx = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for p in se:
        me = set(p)
        for y, x in p:
            for dy, dx in dydx:
                nynx = (y+dy, x+dx)
                if nynx in me:
                    continue
                q = p+(nynx,)
                min_y = min(y for y, x in q)
                min_x = min(x for y, x in q)
                q = ((y-min_y, x-min_x) for y, x in q)
                q = tuple(sorted(q))
                yield q
