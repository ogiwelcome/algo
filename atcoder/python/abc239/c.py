x1,y1,x2,y2=map(int,input().split())
a=2*(x1-x2)
b=2*(y1-y2)
c=x1**2-x2**2+y1**2-y2**2
flg=False
for dx in range(-5,6):
    for dy in range(-5,6):
        nx1=x1+dx
        ny1=y1+dy
        if (nx1-x1)**2+(ny1-y1)**2==5 and (nx1-x2)**2+(ny1-y2)**2==5:
            flg=True
if flg:
    print("Yes")
else:
    print("No")