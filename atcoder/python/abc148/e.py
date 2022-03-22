n=int(input())
if n%2:
    print(0)
else:
    ans=0
    m=n
    n//=2
    while n>0:
        n//=5
        ans+=n
    print(ans)