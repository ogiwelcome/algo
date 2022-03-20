from math import gcd
a,b=map(int,input().split())
g=gcd(a,b)
cnt=1
for i in range(2,10**6+1):
    if g%i==0:
        cnt+=1
        while g%i==0:
            g//=i
if g>1:
    cnt+=1
print(cnt)