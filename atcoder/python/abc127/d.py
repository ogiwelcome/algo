n,m=map(int,input().split())
a=list(map(int,input().split()))
bc=[list(map(int,input().split())) for i in range(m)]
bc.sort(key=lambda x:-x[1])
arr=[]
for b,c in bc:
    if len(arr)+b<n:
        arr+=[c]*b
    else:
        arr+=[c]*(n-len(arr))
aa=a+arr
aa.sort(reverse=True)
aa=aa[:n]
print(sum(aa))