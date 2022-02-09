from math import ceil,floor
n=int(input())
ans=0
k0=int(n**0.5)
for i in range(1,n//(k0+1)+1):
    ans+=n//i
for k in range(1,k0+1):
    ans+=(n//k-n//(k+1))*k
print(ans)