s=input()
n=len(s)
l=[]
for i in range(n-1):
    if s[i]=="R" and s[i+1]=="L":
        l.append(i)
ans=[0]*n
for i in l:
    cntR=1
    cntL=1
    j,k=i,i+1
    while j>0:
        if s[j]==s[j-1]:
            j-=1
            cntL+=1
        else:
            break
    while k<n-1:
        if s[k]==s[k+1]:
            k+=1
            cntR+=1
        else:
            break
    ans[i+1],ans[i]=(cntR+1)//2+cntL//2,cntR//2+(cntL+1)//2
print(*ans)