from bisect import bisect_left,bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
minus=[]
plus=[]
zero=[]
for aa in a:
    if aa<0:
        minus.append(-aa)
    elif aa==0:
        zero.append(aa)
    else:
        plus.append(aa)
minus=minus[::-1]
l=-10**18
r=10**18
while r-l>1:
    mid=(l+r)//2
    cnt=0
    if mid>=0:
        cnt+=len(zero)*(n-len(zero))+len(zero)*(len(zero)-1)//2+len(plus)*len(minus)
        idx=len(plus)-1
        for i in range(len(plus)):
            while idx>=0 and plus[idx]*plus[i]>mid:
                idx-=1
            cnt+=max(idx-i,0)
        idx=len(minus)-1
        for i in range(len(minus)):
            while idx>=0 and minus[idx]*minus[i]>mid:
                idx-=1
            cnt+=max(idx-i,0)
    else:
        idx=0
        for i in range(len(plus))[::-1]:
            while idx<len(minus) and plus[i]*minus[idx]<-mid:
                idx+=1
            cnt+=len(minus)-idx
    if cnt>=k:
        r=mid
    else:
        l=mid
print(r)