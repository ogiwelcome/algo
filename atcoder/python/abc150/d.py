from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
cnt2=[0]*n
for i in range(n):
    tar=a[i]
    while tar%2==0:
        cnt2[i]+=1
        tar//=2
cnt2.sort()
if cnt2[0]!=cnt2[-1]:
    print(0)
    exit()
v=a[0]//2
for i in range(1,n):
    v=lcm(v,a[i]//2)
print(m//v-m//(2*v))