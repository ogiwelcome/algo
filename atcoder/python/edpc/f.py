s=input()
ls=len(s)
t=input()
lt=len(t)
dp=[[0]*(lt+1) for i in range(ls+1)]
for i in range(ls):
    for j in range(lt):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
x=ls-1
y=lt-1
ans=[]
while x>=0 and y>=0:
    if s[x]==t[y]:
        ans.append(s[x])
        x-=1
        y-=1
    elif dp[x+1][y+1]==dp[x][y+1]:
        x-=1
    elif dp[x+1][y+1]==dp[x+1][y]:
        y-=1
ans="".join(ans[::-1])
print(ans)