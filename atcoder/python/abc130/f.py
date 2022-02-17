n=int(input())
q=[]
for i in range(n):
    x,y,d=input().split()
    x=int(x)
    y=int(y)
    q.append([x,y,d])
INF=10**10
def ans(t):
    xx=[]
    yy=[]
    for x,y,d in q:
        if d=="L":
            x-=t
        elif d=="R":
            x+=t
        elif d=="U":
            y+=t
        else:
            y-=t
        xx.append(x)
        yy.append(y)
    return (max(xx)-min(xx))*(max(yy)-min(yy))
MIN=0
MAX=INF
while MAX-MIN>=1:
    mid=(MAX+MIN)//2
    s1=ans(mid)
    s2=ans(mid+0.5)
    if s1>s2:
        MIN=mid+0.5
    else:
        MAX=mid
print(min(ans(MIN),ans(MAX)))