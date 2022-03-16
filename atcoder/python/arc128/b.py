t=int(input())
INF=10**18
for _ in range(t):
    r,g,b=map(int,input().split())
    a=[[r,g,b],[r,b,g],[g,r,b],[g,b,r],[b,r,g],[b,g,r]]
    ans=INF
    for x,y,z in a:
        if x==y:
            ans=min(ans,x)
        if y>z and (y-z)%3==0:
            s=(y-z)//3
            cnt=s+z+s*2
            ans=min(ans,cnt)
        if x>z and (x-z)%3==0:
            s=(x-z)//3
            cnt=s+z+s*2
            ans=min(ans,cnt)
    if ans==INF:
        print(-1)
    else:
        print(ans)