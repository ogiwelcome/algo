r1,c1,r2,c2=map(int,input().split())
mod=10**9+7
f=[0]*(3*10**6+1)
f[0]=f[1]=1
for i in range(2,3*10**6+1):
    f[i]=f[i-1]*i%mod
def g(a,b):
    x,y,z=f[a+b],f[a],f[b]
    return x*pow(y,mod-2,mod)*pow(z,mod-2,mod)%mod
print((g(r2+1,c2+1)-g(r1,c2+1)-g(r2+1,c1)+g(r1,c1))%mod)