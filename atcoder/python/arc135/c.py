n=int(input())
a=list(map(int,input().split()))
ans=sum(a)
cnt=[0]*31
for aa in a:
    for j in range(31):
        if (aa>>j)&1:
            cnt[j]+=1
for aa in a:
    sc=0
    for j in range(31):
        if (aa>>j)&1:
            c0=n-cnt[j]
            sc+=(1<<j)*c0
        else:
            c1=cnt[j]
            sc+=(1<<j)*c1
    if sc>ans:
        ans=sc
print(ans)