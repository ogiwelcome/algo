import sys
sys.setrecursionlimit(10**6)
n = int(input())
p = [list(map(int,input().split())) for i in range(n)]
g = [[] for i in range(10**6)]
for x,y in p:
    x-=1
    y=y-1+10**5
    g[x].append(y)
    g[y].append(x)
used = set()
def dfs(x,y,node):
    if node in used:
        return x,y
    if node<10**5:
        x+=1
    else:
        y+=1
    used.add(node)
    for nxt in g[node]:
        x,y = dfs(x,y,nxt)
    return x,y
ans=0
for i in range(10**5):
    x,y = dfs(0,0,i)
    ans+=x*y
print(ans-n)