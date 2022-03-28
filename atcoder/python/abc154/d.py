n,k=map(int,input().split())
p=list(map(int,input().split()))
s=0
for i in range(k):
    s+=(p[i]+1)/2
ans=s
for i in range(k,n):
    s+=(p[i]+1)/2-(p[i-k]+1)/2
    ans=max(ans,s)
print(ans)