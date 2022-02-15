mod=10**9+7
N=10**6
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
n,m,k=map(int,input().split())
cmb=comb(n*m-2,k-2,mod)
ans=0
for dx in range(1,m):
    cnt=(m-dx)*n*n
    sc=dx*cnt*cmb%mod
    ans+=sc
    ans%=mod
for dy in range(1,n):
    cnt=(n-dy)*m*m
    sc=dy*cnt*cmb%mod
    ans+=sc
    ans%=mod
print(ans)