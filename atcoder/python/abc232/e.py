def mat_mul(a, b, mod=998244353):
    r = [[0]*len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])):
                r[i][j] += a[i][k]*b[k][j]
                r[i][j] %= mod
    return r
def mat_pow(a, n):
    r = [[0]*len(a) for i in range(len(a))]
    b = []
    for i in range(len(a)):
        r[i][i] = 1
        b.append(a[i][:])
    l = n
    while l:
        if l & 1:
            r = mat_mul(b, r)
        b = mat_mul(b, b)
        l >>= 1
    return r
h,w,k=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
mod=998244353
A=[[h+w-4,h-1,w-1,0],[1,w-2,0,w-1],[1,0,h-2,h-1],[0,1,1,0]]
A_k=mat_pow(A,k)
x0=[[0],[0],[0],[0]]
if x1==x2 and y1==y2:
    x0[3][0]=1
elif x1==x2:
    x0[1][0]=1
elif y1==y2:
    x0[2][0]=1
else:
    x0[0][0]=1
ans=mat_mul(A_k,x0)[3][0]%mod
print(ans)