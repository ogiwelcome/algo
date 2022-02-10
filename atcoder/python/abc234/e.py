x=int(input())
INF=10**18
ma=INF
for start in range(0,10):
    if x<=start:
        ma=min(ma,start)
    for d in range(-9,10):
        ss=str(start)
        while True:
            if 1<=int(ss[0])+d<=9:
                ss=str(int(ss[0])+d)+ss
                if int(ss)>=x:
                    ma=min(ma,int(ss))
                    break
            else:
                break
print(ma)