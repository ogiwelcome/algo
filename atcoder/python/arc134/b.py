n=int(input())
s=list(input())
L,R,c=0,n-1,'a'
while c<'z':
    l,r=-1,n
    for i in range(L,R+1):
        if c<s[i]:
            l=i
            break
    for i in range(L,R+1)[::-1]:
        if c==s[i]:
            r=i
            break
    if L<=l<r<=R:
        s[l],s[r]=s[r],s[l]
        L=l+1
        R=r-1
    else:
        c=chr(ord(c)+1)
print(''.join(s))