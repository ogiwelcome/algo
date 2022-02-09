n,k=map(int,input().split())
a=list(map(int,input().split()))
l=0
r=10**18
while r-l>1:
    mid=(l+r)//2
    s=0
    for i in range(n):
        s+=min(mid,a[i])
    if mid*k<=s:
        l=mid
    else:
        r=mid
print(l)