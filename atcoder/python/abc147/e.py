import sys
input=sys.stdin.readline
h,w=map(int,input().split())

a=[list(map(int,input().split())) for i in range(h)]
b=[list(map(int,input().split())) for i in range(h)]
d=[[abs(a[i][j]-b[i][j]) for j in range(w)] for i in range(h)]
dp=[[set() for j in range(w)] for i in range(h)]
dp[0][0].add(d[0][0])
for i in range(h):
    for j in range(w):
        if i+1<=h-1:
            dd=d[i+1][j]
            for num in dp[i][j]:
                dp[i+1][j].add(abs(num+dd))
                dp[i+1][j].add(abs(num-dd))
        if j+1<=w-1:
            dd=d[i][j+1]
            for num in dp[i][j]:
                dp[i][j+1].add(abs(num+dd))
                dp[i][j+1].add(abs(num-dd))
print(min(dp[h-1][w-1]))