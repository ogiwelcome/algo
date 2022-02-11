q=int(input())
n=2**20
a=[-1]*n
r=[(i+1)%n for i in range(n)]
for _ in range(q):
    t,x=map(int,input().split())
    if t==1:
        h=x%n
        nh=x%n
        while a[nh]!=-1:
            nh=r[nh]
        a[nh]=x
        r[h]=(nh+1)%n
    else:
        print(a[x%n])
