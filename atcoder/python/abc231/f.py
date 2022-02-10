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
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
idx={e:i+1 for i,e in enumerate(sorted(set(b)))}
bb=[idx[b[i]] for i in range(n)]
ab=[(a[i],bb[i]) for i in range(n)]
ab.sort(key=lambda x:(x[0],-x[1]))
ans=0
bit=BIT(n+1)
i=0
while i<n:
    _,b=ab[i]
    j=i
    while j<n and ab[i]==ab[j]:
        j+=1
    cnt=j-i
    bit.add(b,cnt)
    ans+=(bit.sum(n)-bit.sum(b-1))*cnt
    i=j
print(ans)