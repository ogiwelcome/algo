x,y=map(int,input().split())
mod=10**9+7
if 2*y-x>=0 and 2*x-y>=0 and (2*x-y)%3==0 and (2*y-x)%3==0:
    s=(2*y-x)//3
    t=(2*x-y)//3
    ans=1
    inv=[0]+[pow(i,mod-2,mod) for i in range(1,t+1)]
    for i in range(1,t+1):
        ans*=(s+i)*inv[i]%mod
        ans%=mod
    print(ans)
else:
    print(0)