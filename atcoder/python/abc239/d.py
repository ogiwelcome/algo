a,b,c,d=map(int,input().split())
sosu=set()
for i in range(2,1000):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        sosu.add(i)
for i in range(a,b+1):
    flg=True
    for j in range(c,d+1):
        if i+j in sosu:
            flg=False
    if flg:
        print("Takahashi")
        exit()
print("Aoki")