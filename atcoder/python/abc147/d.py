n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
c=[[0]*2 for i in range(61)]
ans=0
for j in range(61):
    for i in range(n):
        if (a[i]>>j)&1:
            c[j][1]+=1
        else:
            c[j][0]+=1
for i in range(61):
    ans+=(1<<i)*c[i][0]*c[i][1]%mod
    ans%=mod
print(ans)