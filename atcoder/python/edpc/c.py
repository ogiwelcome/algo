n=int(input())
abc=[list(map(int,input().split())) for i in range(n)]
dp=[[0]*3 for i in range(n+1)]
for i in range(n):
    a,b,c=abc[i]
    dp[i+1][0]=max(dp[i][1],dp[i][2])+a
    dp[i+1][1]=max(dp[i][0],dp[i][2])+b
    dp[i+1][2]=max(dp[i][0],dp[i][1])+c
print(max(dp[-1]))