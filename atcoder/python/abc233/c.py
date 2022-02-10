n,x=map(int,input().split())
l=[]
a=[]
for i in range(n):
    ai=list(map(int,input().split()))
    l.append(ai[0])
    a.append(ai[1:])
dp=[{} for i in range(n)]
for aa in a[0]:
    dp[0][aa]=dp[0].get(aa,0)+1
for i in range(1,n):
    for px in dp[i-1].keys():
        for aa in a[i]:
            if aa*px<=x:
                dp[i][aa*px]=dp[i].get(px*aa,0)+dp[i-1].get(px,0)
print(dp[-1].get(x,0))