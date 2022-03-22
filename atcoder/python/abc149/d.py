n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
ans=0
for i in range(k):
    x=i
    cnt=0
    while x+k<n:
        if t[x]==t[x+k]:
            cnt+=1
        else:
            if t[x]=="r":
                ans+=p*(cnt//2+1)
            elif t[x]=="s":
                ans+=r*(cnt//2+1)
            else:
                ans+=s*(cnt//2+1)
            cnt=0
        x+=k
    if t[x]=="r":
        ans+=p*(cnt//2+1)
    elif t[x]=="s":
        ans+=r*(cnt//2+1)
    else:
        ans+=s*(cnt//2+1)
print(ans)