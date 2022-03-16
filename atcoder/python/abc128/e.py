from heapq import heappop,heappush
n,q=map(int,input().split())
stx=[list(map(int,input().split())) for i in range(n)]
d=[int(input()) for _ in range(q)]
event=[]
for s,t,x in stx:
    event.append([s-x,0,x])
    event.append([t-x,1,x])
for i in range(q):
    event.append([d[i],2,0])
event.sort()
closed=set()
hq=[]
for t,flg,p in event:
    if flg==1:
        closed.remove(p)
    elif flg==0:
        heappush(hq,p)
        closed.add(p)
    else:
        while hq and (hq[0] not in closed):
            heappop(hq)
        if hq:
            print(hq[0])
        else:
            print(-1)