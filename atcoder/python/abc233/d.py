from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
dd=defaultdict(int)
dd[0]=1
ans=0
sa=0
for aa in a:
    sa+=aa
    ans+=dd[sa-k]
    dd[sa]+=1
print(ans)