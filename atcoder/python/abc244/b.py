n=int(input())
s=list(input())
d=["R","D","L","U"]
now=0
x=0
y=0
for ss in s:
    if ss=="S":
        if d[now]=="R":
            x+=1
        if d[now]=="L":
            x-=1
        if d[now]=="U":
            y+=1
        if d[now]=="D":
            y-=1
    else:
        now=(now+1)%4
print(x,y)