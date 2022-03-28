k,q=map(int,input().split())
d=list(map(int,input().split()))
for _ in range(q):
    n,x,m=map(int,input().split())
    dd=d[:]
    for i in range(len(dd)):
        dd[i]%=m
        if dd[i]==0:
            dd[i]=m
    s=x%m+sum(dd)*((n-1)//k)+sum(dd[:(n-1)%k])
    print(n-1-s//m)