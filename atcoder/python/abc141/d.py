from heapq import heappop,heappush
n,m=map(int,input().split())
a=list(map(int,input().split()))
hq=[]
for i in range(n):
    heappush(hq,-a[i])
while m>0:
    x=-heappop(hq)
    x//=2
    heappush(hq,-x)
    m-=1
print(-sum(hq))