n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7
dp=[0]*(k+1)
sdp=[1]*(k+1)
dp[0]=1
for i in range(n):
    for j in range(k+1):
        if j-a[i]-1>=0:
            dp[j]=sdp[j]-sdp[j-a[i]-1]
        else:
            dp[j]=sdp[j]
        dp[j]%=mod
    sdp=dp[:]
    for j in range(k):
        sdp[j+1]+=sdp[j]
        sdp[j+1]%=mod
print(dp[k])