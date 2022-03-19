import heapq
n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(key=lambda x:x[0])
ans=0
hq=[]
e=0
for i in range(1,m+1):
    while e<n and ab[e][0]==i:
        heapq.heappush(hq,-ab[e][1])
        e+=1
    if hq:
        ans-=heapq.heappop(hq)
print(ans)