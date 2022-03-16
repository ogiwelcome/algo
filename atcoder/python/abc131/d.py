from re import A


n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
ab.sort(key=lambda x:x[1])
now = 0
for i in range(n):
    ai,bi=ab[i]
    if now+ai>bi:
        print("No")
        exit()
    now+=ai
print("Yes")