n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
f.sort(reverse=True)
l=0
r=10**18
while r-l>1:
    mid=(l+r)//2
    cnt=0
    for i in range(n):
        if a[i]*f[i]>mid:
            d=(a[i]*f[i]-mid+f[i]-1)//f[i]
            cnt+=d
    if cnt>k:
        l=mid
    else:
        r=mid
if r==1:
    print(0)
else:
    print(r)