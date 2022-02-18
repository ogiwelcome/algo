a=list(input())
b=list(input())
la=len(a)
lb=len(b)
ca=[0]*10
cb=[0]*10
for i in range(la):
    a[i]=int(a[i])
    ca[a[i]]+=1
for i in range(lb):
    b[i]=int(b[i])
    cb[b[i]]+=1
if la<lb:
    ca[0]+=lb-la
else:
    cb[0]+=la-lb
ll=max(la,lb)
max_k=-1
max_pair=[]
for a0 in range(1,10):
    pair=[]
    if ca[a0]==0:
        continue
    ca2=ca[:]
    ca2[a0]-=1
    cb2=cb[:]
    for b0 in range(1,10):
        if a0+b0>=10 and cb2[b0]>0:
            cb2[b0]-=1
            pair.append([a0,b0])
            break
    else:
        if max_k>=0:
            continue
        for i in range(ll):
            ai=a[i] if i<la else 0
            bi=b[i] if i<lb else 0
            pair.append([ai,bi])
        max_k=0
        max_pair=pair[::]
        continue
    nk=0 # max_kを記録
    for ai in range(1,10):
        for bi in range(1,10):
            if ai+bi<9:
                continue
            if ca2[ai]>0 and cb2[bi]>0:
                mc=min(ca2[ai],cb2[bi])
                ca2[ai]-=mc
                cb2[bi]-=mc
                nk+=mc
                pair.extend([[ai,bi] for _ in range(mc)])
    if cb2[0]>0 and ca2[9]>0:
        mc=min(ca2[9],cb2[0])
        ca2[9]-=mc
        cb2[0]-=mc
        nk+=mc
        pair.extend([[9,0] for _ in range(mc)])
    if cb2[9]>0 and ca2[0]>0:
        mc=min(ca2[0],cb2[9])
        ca2[0]-=mc
        cb2[9]-=mc
        nk+=mc
        pair.extend([[0,9] for _ in range(mc)])
    if nk>max_k:
        ra=[]
        rb=[]
        for i in range(1,10):
            if ca2[i]>0:
                ra.extend([i]*ca2[i])
            if cb2[i]>0:
                rb.extend([i]*cb2[i])
        if len(ra)<len(rb):
            for i in range(len(ra)):
                pair.append([ra[i],rb[i]])
            for i in range(len(ra),len(rb)):
                pair.append([0,rb[i]])
        else:
            for i in range(len(rb)):
                pair.append([ra[i],rb[i]])
            for i in range(len(rb),len(ra)):
                pair.append([ra[i],0])
        max_k=nk
        max_pair=pair[:]
max_pair=max_pair[::-1]
ans_a=[]
ans_b=[]
for aa,bb in max_pair:
    if aa!=0:
        ans_a.append(str(aa))
    if bb!=0:
        ans_b.append(str(bb))
print("".join(ans_a))
print("".join(ans_b))