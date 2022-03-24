mod=10**9+7
N=10**5
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
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(1,n+1):
    ans+=a[i-1]*(comb(i-1,k-1,mod)-comb(n-i,k-1,mod))%mod
    ans%=mod
print(ans)