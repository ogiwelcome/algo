n=int(input())
a=[list(map(lambda x:int(x)-1,input().split())) for i in range(n)]
cnt=[0]*n
s=set([i for i in range(n)])
ans=-1
while s:
    news=set()
    for i in s:
        if cnt[i]==n-1:
            continue
        pair=a[i][cnt[i]]
        if a[pair][cnt[pair]]==i:
            news.add(i)
            news.add(pair)
    for i in news:
        cnt[i]+=1
    s=news
    ans+=1
if all(i==n-1 for i in cnt):
    print(ans)
else:
    print(-1)