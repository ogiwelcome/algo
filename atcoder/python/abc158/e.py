from collections import defaultdict
n,p=map(int,input().split())
s=input()
if p==2:
    ans=0
    for i in range(n):
        if int(s[i])%2==0:
            ans+=i+1
    print(ans)
    exit()
if p==5:
    ans=0
    for i in range(n):
        if int(s[i])%5==0:
            ans+=i+1
    print(ans)
    exit()
dd=defaultdict(int)
now=0
ans=0
p10=[0]*(n+1)
p10[0]=1
for i in range(n):
    p10[i+1]=p10[i]*10%p
cs=[0]*(n+1)
for i in range(n):
    x=int(s[n-1-i])
    cs[i+1]=(cs[i]+x*p10[i])%p
ans=0
for i in range(n+1):
    ans+=dd[cs[i]]
    dd[cs[i]]+=1
print(ans)