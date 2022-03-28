n=int(input())
a=list(map(int,input().split()))
s=set(a)
for i in range(10**6):
    if i not in s:
        print(i)
        exit()