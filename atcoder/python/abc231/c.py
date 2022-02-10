from bisect import bisect_left
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for _ in range(q):
    x=int(input())
    idx=bisect_left(a,x)
    print(n-idx)