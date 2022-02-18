from collections import defaultdict
n=int(input())
a=[0]+list(map(int,input().split()))
mod=998244353
dd=defaultdict(int)
f=[0]*(n+1)
sa=0
for i in range(n+1):
    sa+=a[i]
    f[i]=dd[sa]
    dd[sa]=i
dp=[0]*(n+1)
dp[1]=1
for i in range(1,n):
    dp[i+1]+=dp[i]*2-dp[f[i]]
    dp[i+1]%=mod
print(dp[n])