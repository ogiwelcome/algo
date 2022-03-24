from collections import deque
h,w=map(int,input().split())
s=[input() for i in range(h)]
dy=[1,0,-1,0]
dx=[0,1,0,-1]
ans=0
INF=10**9
for sy in range(h):
    for sx in range(w):
        if s[sy][sx]=="#":continue
        dq=deque([[sy,sx]])
        d=[[INF]*w for i in range(h)]
        d[sy][sx]=0
        while dq:
            y,x=dq.popleft()
            for i in range(4):
                ny=y+dy[i]
                nx=x+dx[i]
                if 0<=ny<h and 0<=nx<w and s[ny][nx]=="." and d[ny][nx]==INF:
                    d[ny][nx]=d[y][x]+1
                    dq.append([ny,nx])
                    if ans<d[ny][nx]:
                        ans=max(ans,d[ny][nx])
print(ans)