n,k = map(int,input().split())
mod = 10**9+7
m=10**5
num = [0]*m
i=1
iter=0
while i<=n:
    j=n//i
    if i<=j:
        num[iter]=1
        i+=1
    else:
        num[iter]=n//j-i+1
        i=n//j+1
    iter+=1
dp = [[0]*m for i in range(k+1)]
dp[0][0]=1
for i in range(k):
    sdp=[0]*(iter+1)
    for j in range(iter):
        sdp[j+1]=sdp[j]+dp[i][j]
        sdp[j+1]%=mod
    for j in range(iter):
        dp[i+1][j]=sdp[iter-j]*num[j]%mod
ans = sum(dp[k])%mod
print(ans)