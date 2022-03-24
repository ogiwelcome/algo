n=int(input())
c=list(map(int,input().split()))
mod=10**9+7
c.sort(reverse=True)
ans=0
for i in range(n):
    ans+=c[i]*(i+2)
    ans%=mod
ans*=pow(2,2*n-2,mod)
ans%=mod
print(ans)