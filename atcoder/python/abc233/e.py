x=list(input())
n=len(x)
for i in range(n):
    x[i]=int(x[i])
sx=[x[i] for i in range(n)]
for i in range(n-1):
    sx[i+1]+=sx[i]
ans=[]
amari=0
for i in range(n)[::-1]:
    xx=sx[i]+amari
    d=xx//10
    r=xx%10
    ans.append(str(r))
    if d:
        amari=d
    else:
        amari=0
if amari:
    ans.append(str(amari))
ans=ans[::-1]
print("".join(ans))