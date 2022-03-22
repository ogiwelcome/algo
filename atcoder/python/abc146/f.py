n,m=map(int,input().split())
s=input()
s=s[::-1]
arr=[]
now=0
while now<n:
    nxt=-1
    for i in range(1,m+1):
        if now+i==n:
            arr.append(i)
            print(*arr[::-1])
            exit()
        if now+i<n and s[now+i]=="0":
            nxt=now+i
    if nxt==-1:
        print(-1)
        exit()
    else:
        arr.append(nxt-now)
        now=nxt
