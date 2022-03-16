from collections import defaultdict as dd
h,w,n=map(int,input().split())
rca=[list(map(int,input().split())) for i in range(n)]
p=dd(list)
vals=set()
for i in range(n):
    ri,ci,ai=rca[i]
    p[ai].append([ri,ci,i])
    vals.add(ai)
vals=sorted(list(vals),reverse=True)
rm=[0]*(h+1)
cm=[0]*(w+1)
dp=[0]*n
for x in vals:
    for ri,ci,idx in p[x]:
        dp[idx]=max(rm[ri],cm[ci])
    for ri,ci,idx in p[x]:
        rm[ri]=max(rm[ri],dp[idx]+1)
        cm[ci]=max(cm[ci],dp[idx]+1)
print(*dp,sep="\n")