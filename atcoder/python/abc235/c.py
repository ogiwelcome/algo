from collections import defaultdict
n,q=map(int,input().split())
a=list(map(int,input().split()))
idx=defaultdict(list)
for i in range(n):
    idx[a[i]].append(i)
for _ in range(q):
    x,k=map(int,input().split())
    if len(idx[x])<k:
        print(-1)
    else:
        print(idx[x][k-1]+1)