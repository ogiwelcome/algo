h,w=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
b=[[a[i][j] for i in range(h)] for j in range(w)]
for bb in b:
    print(*bb)