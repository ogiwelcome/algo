from collections import defaultdict
n,x,d=map(int,input().split())
if d==0:
    print(1 if x==0 else n+1)
    exit()
if d<0:
    x,d=-x,-d
dd=defaultdict(list)
for k in range(n+1):
    left=k*x+k*(k-1)//2*d
    right=k*x+k*(2*n-k-1)//2*d
    dd[left%d].append([left,right])
ans=0
for lr in dd.values():
    lr.sort()
    cur=-10**18
    for l,r in lr:
        if cur<l:
            ans+=(r-l)//d+1
            cur=r
        if cur<r:
            ans+=(r-cur)//d
            cur=r
print(ans)