n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
flg=True
use=[0]*n
for j in range(m):
    for i in range(n):
        if a[i]==b[j] and use[i]==0:
            use[i]=1
            break
    else:
        flg=False
        break
if flg:
    print("Yes")
else:
    print("No")