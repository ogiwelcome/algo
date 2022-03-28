n,a,b=map(int,input().split())
mod=10**9+7
ans=(pow(2,n,mod)-1)%mod
cmb_a=1
for i in range(1,a+1):
    cmb_a*=(n-i+1)*pow(i,mod-2,mod)
    cmb_a%=mod
cmb_b=1
for i in range(1,b+1):
    cmb_b*=(n-i+1)*pow(i,mod-2,mod)
    cmb_b%=mod
ans-=cmb_a+cmb_b
ans%=mod
print(ans)