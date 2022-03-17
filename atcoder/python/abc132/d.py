def comb(n,k,p):
  from math import factorial
  if n<0 or k<0 or n<k:return 0
  if n==0 and k==0:return 1
  a=factorial(n)%p
  b=factorial(k)%p
  c=factorial(n-k)%p
  return (a*power_func(b,p-2,p)*power_func(c,p-2,p))%p
def power_func(a,b,p):
  if b==0:
    return 1
  if b%2==0:
    d=power_func(a,b//2,p)
    return (d*d)%p
  else:
    return (a*power_func(a,b-1,p))%p
n,k = map(int,input().split())
mod=10**9+7
for i in range(1,k+1):
    ans=0
    if n-k-(i-1)>=0:
        ans+=comb(k-1,i-1,mod)*comb(n-k+1,i,mod)%mod
        ans%=mod
    print(ans)