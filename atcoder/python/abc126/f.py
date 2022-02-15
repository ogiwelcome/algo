m,k=map(int,input().split())
if k>=2**m:
    print(-1)
elif m==0:
    if k!=0:
        print(-1)
    else:
        print(0,0)
elif m==1:
    if k!=0:
        print(-1)
    else:
        print(0,0,1,1)
else:
    arr=[]
    if k==0:
        for i in range(2**m):
            arr+=[i,i]
    else:
        arr1=[i for i in range(2**m) if i!=k]
        arr2=arr1[::-1]
        arr=arr1+[k]+arr2+[k]
    print(*arr)