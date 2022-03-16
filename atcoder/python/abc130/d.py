from bisect import bisect_left,bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
sa=[a[i] for i in range(n)]
for i in range(n-1):
    sa[i+1]+=sa[i]
ans=0
for i in range(n):
    if sa[i]<k:
        continue
    r=sa[i]-k
    idx=bisect_right(sa,r)+1
    ans+=idx
print(ans)