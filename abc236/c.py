n,m=map(int,input().split())
s=map(str,input().split())
t=map(str,input().split())
tt=set(t)
for ss in s:
    if ss in tt:
        print("Yes")
    else:
        print("No")