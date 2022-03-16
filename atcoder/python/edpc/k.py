n,k=map(int,input().split())
a=list(map(int,input().split()))
# dp_i: i個の山から操作を始める時にどちらが勝つか
dp=[0]*(k+1)
for i in range(k+1):
    for aa in a:
        if i-aa>=0 and dp[i-aa]==0:
            dp[i]=1
if dp[k]==1:
    print("First")
else:
    print("Second")