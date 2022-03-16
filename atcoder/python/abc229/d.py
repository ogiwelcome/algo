s=list(input())
x=int(input())
n=len(s)
l=0
r=n+1
while l+1<r:
    mid=(l+r)//2
    cnt=0
    for i in range(mid):
        if s[i]=="X":
            cnt+=1
    flg=(cnt+x>=mid)
    for i in range(mid,n):
        if s[i-mid]=="X":
            cnt-=1
        if s[i]=="X":
            cnt+=1
        if cnt+x>=mid:
            flg=True
    if flg:
        l=mid
    else:
        r=mid
print(l)