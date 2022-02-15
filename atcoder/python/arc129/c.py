n=int(input())
# greedyでciを決める
c=[0]*7
s=n
for i in range(7):
    cnt=0
    while cnt*(cnt+1)//2 <= s:
        cnt+=1
    s-=cnt*(cnt-1)//2
    if cnt==1:
        cnt=0
    c[i]=cnt
c[0]-=1
use=[]
for i in range(7):
    use+=[i]*c[i]
ans=[]
tmp=0
p=1
for c in use:
    for j in range(1,8):
        if (tmp+p*j)%7==c:
            ans.append(str(j))
            tmp+=p*j
            break
    p=(p*10)%7
print("".join(ans[::-1]))