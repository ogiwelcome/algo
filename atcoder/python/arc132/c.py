from collections import defaultdict
n,d=map(int,input().split())
a=list(map(int,input().split()))
for i in range(len(a)):
    a[i]-=1
mod=998244353
dp=[[0]*(2**(2*d+1)) for i in range(n+1)]
dp[0][(1<<(d+1))-1]=1
for i in range(n):
    for si in range(1<<(2*d+1)):
        if si&1==0:
            continue
        ns=si>>1
        for j in range(2*d+1):
            if (ns>>j)&1:
                continue
            if 0<=i-d+j<n and (a[i]==-2 or a[i]==i-d+j):
                dp[i+1][ns|(1<<j)]+=dp[i][si]
                dp[i+1][ns|(1<<j)]%=mod
print(dp[n][(1<<(d+1))-1])