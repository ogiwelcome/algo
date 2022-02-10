s=list(input())
n=len(s)
flg=True
for i in range(n//2):
    if s[i]!=s[n-1-i]:
        flg=False
if flg:
    print("Yes")
    exit()
l=0
r=n-1
while l+1<n and s[l]=="a" and s[r]=="a":
    l+=1
    r-=1
s=s[l:r+1]
n=len(s)
flg=True
for i in range(n)[::-1]:
    if s[i]!="a":
        x=i+1
        for j in range(x//2):
            if s[j] != s[x-1-j]:
                flg=False
                break
        break

if flg:
    print("Yes")
else:
    print("No")