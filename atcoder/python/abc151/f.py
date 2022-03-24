n=int(input())
p=[list(map(int,input().split())) for i in range(n)]
if n==2:
    print(((p[0][0]-p[1][0])**2+(p[0][1]-p[1][1])**2)**0.5/2)
    exit()
def min_c(x1,y1,x2,y2,x3,y3):
    d1=(x2-x3)**2+(y2-y3)**2
    d2=(x1-x3)**2+(y1-y3)**2
    d3=(x1-x2)**2+(y1-y2)**2
    d1,d2,d3=sorted([d1,d2,d3],reverse=True)
    if d1>=d2+d3:
        return d1**0.5/2
    d1**=0.5 
    d2**=0.5
    d3**=0.5
    cosa=(d2**2+d3**2-d1**2)/(2*d2*d3)
    sina=(1-cosa**2)**0.5
    return d1/2/sina
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1,y1=p[i]
            x2,y2=p[j]
            x3,y3=p[k]
            ans=max(ans,min_c(x1,y1,x2,y2,x3,y3))
print(ans)