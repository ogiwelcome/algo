from heapq import heappop, heappush
n,k=map(int,input().split())
p=list(map(int,input().split()))
hq = []
for i in range(k):
    heappush(hq,p[i])
print(min(p[:k]))
for i in range(k,n):
    x=heappop(hq)
    if x<p[i]:
        heappush(hq,p[i])
    else:
        heappush(hq,x)
    ans=heappop(hq)
    print(ans)
    heappush(hq,ans)