n=int(input())
a=list(map(int,input().split()))
c=[0]*3
for i in range(n):
    c[a[i]-1]+=1
dp=[[[-1]*301 for i in range(301)] for j in range(301)]
def f(c1,c2,c3):
    if dp[c1][c2][c3]>=0:
        return dp[c1][c2][c3]
    if c1<0 or c2<0 or c3<0:
        return 0
    if c1==0 and c2==0 and c3==0:
        return 0
    p=n
    if c1>0:
        p+=f(c1-1,c2,c3)*c1
    if c2>0:
        p+=f(c1+1,c2-1,c3)*c2
    if c3>0:
        p+=f(c1,c2+1,c3-1)*c3
    p/=(c1+c2+c3)
    dp[c1][c2][c3]=p
    return p
print(f(c[0],c[1],c[2]))