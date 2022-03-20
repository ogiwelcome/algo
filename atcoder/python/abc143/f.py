n=int(input())
a=list(map(int,input().split()))
c=[0]*(n+1)
for i in a:
    c[i]+=1
d=[0]*(n+1)
for cc in c:
    d[cc]+=1
sd=d[:]
skd=[k*d[k] for k in range(n+1)]
for i in range(len(d)-1):
    sd[i+1]+=sd[i]
    skd[i+1]+=skd[i]
f=[0]*n
for x in range(1,n+1):
    f[x-1]=(skd[x]+x*(sd[n]-sd[x]))//x
for k in range(1,n+1):
    l=-1
    r=len(f)
    while r-l>1:
        mid=(l+r)//2
        if f[mid]>=k:
            l=mid
        else:
            r=mid
    print(l+1)