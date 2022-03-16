n,d=map(int,input().split())
lr=[list(map(int,input().split())) for i in range(n)]
lr.sort(key=lambda x:x[1])
cnt=1
left=lr[0][1]
right=lr[0][1]+d-1
now=0
while now<n:
    nl,nr=lr[now]
    if right<nl:
        left=lr[now][1]
        right=lr[now][1]+d-1
        cnt+=1
    now+=1
print(cnt)