n=int(input())
s=[list(input()) for i in range(n)]
flg=False
for i in range(n):
    for j in range(n):
        cnt=0
        for dy in range(6):
            ii=i+dy
            if ii>=n:
                cnt+=100
                break
            if s[ii][j]==".":
                cnt+=1
        if cnt<=2:
            flg=True
        cnt=0
        for dx in range(6):
            jj=j+dx
            if jj>=n:
                cnt+=100
                break
            if s[i][jj]==".":
                cnt+=1
        if cnt<=2:
            flg=True
        cnt=0
        for dd in range(6):
            ii=i+dd
            jj=j+dd
            if ii>=n or jj>=n:
                cnt+=100
                break
            if s[ii][jj]==".":
                cnt+=1
        if cnt<=2:
            flg=True
        cnt=0
        for dd in range(6):
            ii=i-dd
            jj=j+dd
            if not (0<=ii<n and 0<=jj<n):
                cnt+=100
                break
            if s[ii][jj]==".":
                cnt+=1
        if cnt<=2:
            flg=True
        cnt=0
        for dd in range(6):
            ii=i+dd
            jj=j-dd
            if not (0<=ii<n and 0<=jj<n):
                cnt+=100
                break
            if s[ii][jj]==".":
                cnt+=1
        if cnt<=2:
            flg=True
        cnt=0
        for dd in range(6):
            ii=i-dd
            jj=j-dd
            if not (0<=ii<n and 0<=jj<n):
                cnt+=100
                break
            if s[ii][jj]==".":
                cnt+=1
        if cnt<=2:
            flg=True
if flg:
    print("Yes")
else:
    print("No")