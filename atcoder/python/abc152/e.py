from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
ans=0
for i in range(n):
    ans+=pow(a[i],mod-2,mod)
dd=defaultdict(int)
for i in range(n):
    aa=a[i]
    for j in range(2,10**3+1):
        if aa<j:
            break
        if aa%j==0:
            cnt=0
            while aa%j==0:
                aa//=j
                cnt+=1
            dd[j]=max(dd[j],cnt)
    if aa>1:
        dd[aa]=max(dd[aa],1)
lcm=1
for key,val in dd.items():
    p=pow(key,val,mod)
    lcm*=p
    lcm%=mod
print(ans*lcm%mod)