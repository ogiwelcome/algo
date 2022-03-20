from math import atan2
n=int(input())
p=[]
for i in range(n):
    x,y=map(int,input().split())
    if x==y==0:
        continue
    p.append([x,y])
if not p:
    print(0)
    exit()
n=len(p)
p.sort(key=lambda x:atan2(x[1],x[0]))
p=p+p
ans=0
for i in range(n):
    sx=0
    sy=0
    for j in range(i,i+n):
        sx+=p[j][0]
        sy+=p[j][1]
        ans=max(ans,(sx**2+sy**2)**0.5)
print(ans)