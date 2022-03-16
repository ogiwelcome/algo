from math import ceil
from collections import defaultdict
n,y=map(int,input().split())
a=list(map(int,input().split()))
mem=defaultdict(int)
def calc(x, idx): # x円を払うのに必要な最小の枚数を計算
    if mem[x]>0:
        return mem[x]
    if idx==n-1:
        return x//a[n-1]
    if x==0:
        return 0
    cur,nxt=a[idx],a[idx+1]
    r1=x%nxt
    ans=calc(x-r1,idx+1)+r1//cur
    if r1:
        ans=min(ans,calc(x+nxt-r1,idx+1)+(nxt-r1)//cur)
    mem[x]=ans
    return ans
print(calc(y,0))