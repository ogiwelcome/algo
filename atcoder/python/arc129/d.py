n=int(input())
a=list(map(int,input().split()))
if sum(a)!=0 :
    print(-1)
    exit()
b=[0]*n
s=0
for i in range(n-1):
    s+=a[i+1]*(n-1-i)
if s%n!=0:
    print(-1)
    exit()
b[0]=-(s//n)
for i in range(1,n):
    b[i]=b[i-1]+a[i]
sb=0
ans=[0]*n
for i in range(n):
    sb+=b[i]
    if ans[0]+sb<0:
        ans[0]=-sb
for i in range(1,n):
    ans[i]=ans[i-1]+b[i-1]
print(sum(ans))