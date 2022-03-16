from heapq import heappop, heappush
q=int(input())
sc=0
l=[]
r=[]
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        a,b=query[1:]
        sc+=b
        heappush(l,a)
        heappush(r,-a)
        if l[0]<-r[0]:
            x=heappop(l)
            y=-heappop(r)
            sc+=y-x
            heappush(l,y)
            heappush(r,-x)
    else:
        print(-r[0],sc)