n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353
c1=sum(a)-a[0]
if c1+k>a[0]:
    print(0)
    exit()
ans=1
inv_k=[-1]+[pow(i,mod-2,mod) for i in range(1,k+1)]
for i in range(1,n):
    c=a[i]+k-1
    for j in range(1,k):
        ans*=(c+1-j)*inv_k[j]
        ans%=mod
# ここまで1以外の振り分け
r=a[0]-c1-k
if r==0:
    print(ans)
    exit()
s2=r+k-1
for i in range(1,k):
    ans*=s2+1-i
    ans*=pow(i,mod-2,mod)
    ans%=mod
print(ans)