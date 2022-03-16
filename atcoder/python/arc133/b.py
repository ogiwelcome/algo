from bisect import bisect_left, bisect_right
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
idx_q=[-1]*(n+1)
for i in range(n):
    idx_q[q[i]]=i
pair=[]
for i in range(n):
    x=p[i]
    dx=p[i]
    while x<=n:
        idx=idx_q[x]
        pair.append([i,idx])
        x+=dx
pair.sort(key=lambda x:(x[0],-x[1]))
arr=[pair[i][1] for i in range(len(pair))]
l=len(arr)
INF=10**9
LIS=[arr[0]]
for i in range(l):
    if arr[i]>LIS[-1]:
        LIS.append(arr[i])
    else:
        idx=bisect_left(LIS,arr[i])
        LIS[idx]=arr[i]
print(len(LIS))