n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
l=0
r=10**18
while r-l>1:
    mid=(l+r)//2
    cnt=0
    idx=n
    for ai in a:
        while idx>0 and ai+a[idx-1]<mid:
            idx-=1
        cnt+=idx
    if cnt<m:
        r=mid
    else:
        l=mid
sa=[0]+a[:]
for i in range(n):
    sa[i+1]+=sa[i]
res=0
idx=n
for ai in a:
    while idx>0 and ai+a[idx-1]<l:
        idx-=1
    res+=sa[idx]+ai*idx
    m-=idx
if m<0:
    res+=l*m
print(res)