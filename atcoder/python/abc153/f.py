from bisect import bisect_right
from math import ceil
n,d,a=map(int,input().split())
xh=[list(map(int,input().split())) for i in range(n)]
xh.sort(key=lambda x:x[0])
xx=[xh[i][0] for i in range(n)]
damage=[0]*(n+1)
ans=0
for i,(x,h) in enumerate(xh):
    damage[i]+=damage[i-1]
    h-=damage[i]
    if h<=0:
        continue
    cnt=ceil(h/a)
    ans+=cnt
    damage[i]+=a*cnt
    idx=bisect_right(xx,x+2*d)
    damage[idx]-=a*cnt
print(ans)