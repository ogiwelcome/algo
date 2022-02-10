from collections import deque
a,n=map(int,input().split())
m=1
while m<=n:
    m*=10
d=[-1]*m
dq=deque()
d[1]=0
dq.append(1)
while dq:
    v=dq.popleft()
    if a*v<m and d[a*v]==-1:
        d[a*v]=d[v]+1
        dq.append(a*v)
    if v>=10 and v%10!=0:
        s=str(v)
        y=int(s[-1]+s[:-1])
        if y<m and d[y]==-1:
            d[y]=d[v]+1
            dq.append(y)
print(d[n])