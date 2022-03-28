n,k=map(int,input().split())
N=10**6
mod=10**9+7
g1=[1,1]
g2=[1,1]
inv=[0,1]
for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inv.append((-inv[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inv[-1])%mod)
def comb(n,r,mod):
    if r<0 or r>n:
        return 0
    return g1[n]*g2[r]*g2[n-r]%mod
ans=0
for z in range(min(n,k)+1):
    ans+=comb(n,z,mod)*comb(n-1,z,mod)
    ans%=mod
print(ans)