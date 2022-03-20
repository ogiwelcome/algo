from bisect import bisect_left, bisect_right
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(n):
    for j in range(i+1,n):
        a=l[i]
        b=l[j]
        idx=bisect_left(l,a+b)
        ans+=max(0,idx-j-1)
print(ans)