h,w,k=map(int,input().split())
s=[list(input()) for i in range(h)]
ans=10**18
for bit in range(1<<(h-1)):
    arr=[[0]]
    for j in range(h-1):
        if (bit>>j)&1:
            arr.append([j+1])
        else:
            arr[-1].append(j+1)
    idx=[0]*h # それぞれの行がどの区切りに存在するか
    for j in range(len(arr)):
        for x in arr[j]:
            idx[x]=j
    cnt=[[0]*len(arr) for l in range(w)]
    for l in range(w):
        for j in range(h):
            if s[j][l]=="1":
                cnt[l][idx[j]]+=1
    res=0
    c=[0]*len(arr)
    for l in range(w):
        flg=True
        for j in range(len(arr)):
            if c[j]+cnt[l][j]>k:
                flg=False
        if flg:
            for j in range(len(arr)):
                c[j]+=cnt[l][j]
        else:
            res+=1
            for j in range(len(arr)):
                c[j]=cnt[l][j]
            if max(c)>k:
                break
    else:
        ans=min(ans,res+len(arr)-1)
print(ans)