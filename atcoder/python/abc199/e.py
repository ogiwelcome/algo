n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(m)]
rst=[[] for i in range(n+1)]
for x,y,z in xyz:
    rst[x].append([y,z])
dp=[0]*(1<<n)
dp[0]=1
for i in range(1<<n):
    for j in range(n):
        if (i>>j)&1:
            continue
        ii=i^(1<<j)
        tot=[0]*(n+1)
        c=0
        for k in range(n):
            if (ii>>k)&1:
                tot[k+1]+=1
                c+=1
        for k in range(n):
            tot[k+1]+=tot[k]
        flg=True
        for y,z in rst[c]:
            if z<tot[y]:
                flg=False
        if flg:
            dp[ii]+=dp[i]
print(dp[-1])