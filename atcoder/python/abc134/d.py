n = int(input())
a=[0]+list(map(int,input().split()))
cnt=[0]*(n+1)
for i in range(1,n+1)[::-1]:
    s=0
    for j in range(i*2,n+1,i):
        s+=cnt[j]
    cnt[i]=(s+a[i])%2
ans=[]
for i in range(1,n+1):
    if cnt[i]:
        ans.append(i)
print(len(ans))
print(*ans)