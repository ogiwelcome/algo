n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
b=[0]*(m+1)
for i in range(m+1)[::-1]:
    r=0
    for j in range(n+m+1):
        if 0<=n-j<=n and 0<=i+j<=m:
            r+=a[n-j]*b[i+j]
    b[i]=(c[i+n]-r)//a[-1]
print(*b)