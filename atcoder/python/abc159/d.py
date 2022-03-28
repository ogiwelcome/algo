from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
cnt=defaultdict(int)
for aa in a:
    cnt[aa]+=1
ans=0
for key,val in cnt.items():
    ans+=val*(val-1)//2
for i in range(n):
    c1=cnt[a[i]]
    c2=cnt[a[i]]-1
    x=c2*(c2-1)//2-c1*(c1-1)//2+ans
    print(x)