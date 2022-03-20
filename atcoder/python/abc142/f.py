from collections import deque
def bfs(s):
    d=[-1]*n
    d[s]=0
    x={s}
    dq=deque()
    dq.append([s,x])
    flg=False
    while dq:
        p,x = dq.popleft()
        for to in g[p]:
            if d[to]==-1:
                d[to]=d[p]+1
                x.add(to)
                y=x.copy()
                dq.append([to,y])
                x.remove(to)
            elif d[to]==0:
                flg=True
                sc=d[p]+1
            else:
                if to in x:
                    return
        if flg:
            print(sc)
            for v in x:
                print(v+1)
            exit()
    return
n,m=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
for i in range(n):
    bfs(i)
print(-1)