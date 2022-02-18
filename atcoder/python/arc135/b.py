n=int(input())
s=list(map(int,input().split()))
x=[0,0]
for ss in s:
    x.append(ss-x[-1]-x[-2])
c1=-min(x[0::3])
c2=-min(x[1::3])
c3=min(x[2::3])
if c1+c2>c3:
    print("No")
    exit()
a,b=c1,c2
para=[a,b,-a-b]
ans=[x[i]+para[i%3] for i in range(len(x))]
print("Yes")
print(*ans)