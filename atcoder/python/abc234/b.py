n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
    xi,yi=xy[i]
    for j in range(i+1,n):
        xj,yj=xy[j]
        ans=max(ans,((xi-xj)**2+(yi-yj)**2)**0.5)
print(ans)