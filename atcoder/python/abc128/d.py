n,k=map(int,input().split())
v=list(map(int,input().split()))
lv=[0]+[v[i] for i in range(n)]
rv=[0]+[v[i] for i in range(n)][::-1]
for i in range(n):
    lv[i+1]+=lv[i]
    rv[i+1]+=rv[i]
ans=0
for j in range(n+1):
    for l in range(n+1):
        if j+l>k or j+l>n:
            continue
        sc=lv[j]+rv[l]
        have=[]
        for idx in range(j):
            have.append(v[idx])
        for idx in range(l):
            have.append(v[-idx-1])
        have.sort()
        minus=0
        ans=max(ans,sc)
        can_remove=k-(j+l)
        for m in range(min(can_remove,len(have))):
            minus+=have[m]
            ans=max(ans,sc-minus)
print(ans)