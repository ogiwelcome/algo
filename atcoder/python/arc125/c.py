n,k=map(int,input().split())
a=list(map(int,input().split()))
na=set([i for i in range(1,n+1)])-set(a)
na=sorted(list(na),reverse=True)
use=set()
now=1
ans=[]
for i in range(k-1):
    if a[i]==now:
        ans.append(now)
    else:
        ans.append(a[i])
        ans.append(now)
        use.add(a[i])
    use.add(now)
    while now in use:
        now+=1
for i in range(1,n+1)[::-1]:
    if i not in use:
        ans.append(i)
print(*ans)