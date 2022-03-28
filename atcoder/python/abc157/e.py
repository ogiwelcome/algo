class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0] * (n + 1)
    self.el = [0] * (n + 1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j = None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i)
n=int(input())
s=input()
q=int(input())
bits=[BIT(n+1) for i in range(26)]
for i in range(n):
    j=ord(s[i])-ord('a')
    bits[j].add(i+1,1)
for _ in range(q):
    t,x,y=input().split()
    if t=="1":
        x=int(x)
        for i in range(26):
            if bits[i].get(x):
                bits[i].add(x,-1)
        bits[ord(y)-ord('a')].add(x,1)
    else:
        x=int(x)
        y=int(y)
        res=0
        for i in range(26):
            res+=bits[i].get(x-1,y)>0
        print(res)