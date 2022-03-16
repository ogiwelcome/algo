import itertools
n,m=map(int,input().split())
g1=[[] for i in range(n)]
g2=[[] for i in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    g1[a-1].append(b-1)
    g1[b-1].append(a-1)
for _ in range(m):
    c,d=map(int,input().split())
    g2[c-1].append(d-1)
    g2[d-1].append(c-1)
for i in range(n):
    g1[i].sort()
    g2[i].sort()
for idx in list(itertools.permutations([i for i in range(n)],n)):
    flg=True
    for i in range(n):
        if len(g1[i])!=len(g2[idx[i]]):
            flg=False
        g1_idxed=sorted([idx[x] for x in g1[i]])
        if g1_idxed!=g2[idx[i]]:
            flg=False
            break
    if flg:
        print("Yes")
        exit()
print("No")