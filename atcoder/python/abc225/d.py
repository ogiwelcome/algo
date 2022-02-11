n,q=map(int,input().split())
ch=[-1]*n
par=[-1]*n
for _ in range(q):
    query=input().split()
    if query[0]=="1":
        x,y=int(query[1]),int(query[2])
        x-=1
        y-=1
        par[y]=x
        ch[x]=y
    elif query[0]=="2":
        x,y=int(query[1]),int(query[2])
        x-=1
        y-=1
        par[y]=-1
        ch[x]=-1
    else:
        x=int(query[1])
        x-=1
        while par[x]!=-1:
            x=par[x]
        ans=[]
        while x!=-1:
            ans.append(x+1)
            x=ch[x]
        print(len(ans),*ans)