from collections import deque
n=int(input())
edges=[list(map(lambda x:int(x)-1,input().split())) for i in range(n-1)]
g=[[] for i in range(n)]
for i in range(n-1):
    u,v=edges[i]
    g[u].append(v)
dq=deque([0])
col=[0]*n
while dq:
    v=dq.popleft()
    c=1
    for to in g[v]:
        if c==col[v]:
            c+=1
        col[to]=c
        c+=1
        dq.append(to)
print(max(col))
for i in range(n-1):
    print(col[edges[i][1]])