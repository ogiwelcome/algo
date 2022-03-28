def scc(N, G, RG):
    order = []
    state = [0]*N
    traversed, registered = 1, 2
    for i in range(N):
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
    group = [-1]*N
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
    label=max(group)
    size = [0]*(label+1)
    for v in range(N):
        size[group[v]]+=1
    return label, group, size
n,m=map(int,input().split())
g=[[] for i in range(n)]
rg=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    rg[v-1].append(u-1)
label, group, size=scc(n,g,rg)
dp=[0]*(label+1)
ans=0
label_v=[[] for i in range(label+1)]
for i in range(n):
    label_v[group[i]].append(i)
for i in range(label+1)[::-1]:
    if size[i]==1:
        v=label_v[i][0]
        for to in g[v]:
            dp[i]|=dp[group[to]]
    else:
        dp[i]=1
    if dp[i]:
        ans+=size[i]
print(ans)