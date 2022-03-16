h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
l=[[0]*w for i in range(h)]
r=[[0]*w for i in range(h)]
u=[[0]*w for i in range(h)]
d=[[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            l[i][j]=r[i][j]=u[i][j]=d[i][j]=1
for i in range(h):
    for j in range(w-1):
        if s[i][j+1]==".":
            l[i][j+1]+=l[i][j]
    for j in range(1,w)[::-1]:
        if s[i][j-1]==".":
            r[i][j-1]+=r[i][j]
for j in range(w):
    for i in range(h-1):
        if s[i+1][j]==".":
            d[i+1][j]+=d[i][j]
    for i in range(1,h)[::-1]:
        if s[i-1][j]==".":
            u[i-1][j]+=u[i][j]
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            ans=max(ans,l[i][j]+r[i][j]+u[i][j]+d[i][j]-3)
print(ans)