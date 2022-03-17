n,k=map(int,input().split())
if k>(n-1)*(n-2)//2:
    print(-1)
    exit()
edges = []
for i in range(1,n):
    edges.append([1,i+1])
res = (n-1)*(n-2)//2-k
for i in range(1,n):
    for j in range(i+1,n):
        if res>0:
            res-=1
            edges.append([i+1,j+1])
print(len(edges))
for u,v in edges:
    print(u,v)