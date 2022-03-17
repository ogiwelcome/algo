from collections import deque
n,m = map(int,input().split())
g = [[] for i in range(n)]
edges = [list(map(int,input().split())) for i in range(m)]
for u,v in edges:
    g[u-1].append(v-1)
s,t = map(int,input().split())
s-=1
t-=1
dst = [[0]*4 for i in range(n)]
vis=set()
dq = deque([[s,0]])
while dq:
    v,cnt = dq.popleft()
    if v == t and cnt%3 == 0:
        print(dst[v][0]//3)
        exit()
    if (v,cnt) in vis:
        continue
    vis.add((v,cnt))
    cnt2 = (cnt+1)%3
    for to in g[v]:
        if (to,cnt2) not in vis:
            dst[to][cnt2] = dst[v][cnt]+1
            dq.append([to,cnt2])
print(-1)