t=int(input())
for _ in range(t):
    n=int(input())
    s1=set()
    s2=set()
    res=False
    for j in range(n):
        s=input()
        rs=s[::-1]
        if s==rs or s in s1 or s in s2 or s[1:] in s1:
            res=True
        s1.add(rs)
        if len(s)==3:
            s2.add(rs[1:])
    if res:
        print("YES")
    else:
        print("NO")