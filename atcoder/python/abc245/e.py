class BIT:  # 1-indexed
    def __init__(self, n):
        self.n = n
        self.a = [0]*(n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.a[i] += x
            i += i & -i

    def bisect_left(self, x):
        l=s=0
        for i in range(self.n.bit_length(),-1,-1):
            r=l+(1<<i)
            if r<=self.n and s+self.a[r]<x:
                s+=self.a[r]
                l+=1<<i
        return l+1,s
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
itov=sorted(set(a+b+c+d),reverse=True)
vtoi={v:i+1 for i,v in enumerate(itov)}
abcd=[]
for u,v in zip(a,b):
    abcd.append([vtoi[u],vtoi[v],1])
for u,v in zip(c,d):
    abcd.append([vtoi[u],vtoi[v],0])
abcd.sort()
flg=True
bit=BIT(len(itov))
for _, v, x in abcd:
    if x:
        if bit.sum(v)<=0:
            flg=False
        bit.add(bit.bisect_left(bit.sum(v))[0],-1)
    else:
        bit.add(v,1)
if flg:
    print("Yes")
else:
    print("No")