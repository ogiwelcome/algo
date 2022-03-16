T=int(input())
p2=[2**i for i in range(61)]
for _ in range(T):
    a,s=map(int,input().split())
    b=[0]*61
    ss=0
    for i in range(61):
        if (a>>i)&1:
            b[i]=1
            ss+=p2[i]*2
    s-=ss
    if s<0:
        print("No")
        continue
    for i in range(61):
        if (s>>i)&1 and b[i]==1:
            print("No")
            break
    else:
        print("Yes")