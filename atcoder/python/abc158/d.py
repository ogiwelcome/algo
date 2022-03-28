s=list(input())
q=int(input())
l=[]
r=[]
flg=0
for _ in range(q):
    query=list(input().split())
    if query[0]=="1":
        flg^=1
        l,r=r,l
    else:
        f,c=query[1],query[2]
        if f=="1":
            l.append(c)
        else:
            r.append(c)
if flg:
    ans="".join(l[::-1]+s[::-1]+r)
else:
    ans="".join(l[::-1]+s+r)
print(ans)