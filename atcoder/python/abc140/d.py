n,k=map(int,input().split())
s=input()
cnt=0
for i in range(n-1):
    if s[i]=="R" and s[i+1]=="R":
        cnt+=1
    if s[i]=="L" and s[i+1]=="L":
        cnt+=1
print(min(n-1,cnt+2*k))