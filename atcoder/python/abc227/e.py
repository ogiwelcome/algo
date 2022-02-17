from collections import defaultdict
s=list(input())
k=int(input())
l=len(s)
def fix(): return defaultdict(fix)
dp=defaultdict(fix)
dp[0][0][0]=(s,1)
for _ in range(len(s)):
    n_dp=defaultdict(fix)
    for x,d1 in dp.items():
        for e,d2 in d1.items():
            for y,(ss,val) in d2.items():
                for c in "KEY":
                    if c in ss:
                        idx=ss.index(c)
                        xx=x+idx
                        ee=e+(c=="E")
                        yy=y+(c=="Y")
                        if yy in n_dp[xx][ee]:
                            n_dp[xx][ee][yy]=(n_dp[xx][ee][yy][0], n_dp[xx][ee][yy][1]+val)
                        else:
                            n_dp[xx][ee][yy]=(ss[:idx]+ss[idx+1:],val)
    dp=n_dp
ans=0
for x,d1 in dp.items():
    if x>k:
        continue
    for e,d2 in d1.items():
        for y,(ss,val) in d2.items():
            ans+=val
print(ans)