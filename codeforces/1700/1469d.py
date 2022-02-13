from math import ceil
t=int(input())
for _ in range(t):
    n=int(input())
    step=[]
    if n==3:
        step=[[3,2],[3,2]]
    elif n==4:
        step=[[3,4],[4,2],[4,2]]
    elif n<=16:
        for i in range(1,n):
            if i==2 or i==4:
                continue
            step.append([i,n])
        nn=n
        while n>=2:
            n=ceil(n/4)
            step.append([nn,4])
        step.append([4,2])
        step.append([4,2])
    elif n<=64:
        for i in range(1,n):
            if i==2 or i==8:
                continue
            step.append([i,n])
        nn=n
        while n>=2:
            n=ceil(n/8)
            step.append([nn,8])
        step.append([8,2])
        step.append([8,2])
        step.append([8,2])
    else:
        for i in range(1,n):
            if i==2 or i==4 or i==64:
                continue
            step.append([i,n])
        nn=n
        while n>=2:
            n=ceil(n/64)
            step.append([nn,64])
        step.append([64,4])
        step.append([64,4])
        step.append([64,4])
        step.append([4,2])
        step.append([4,2])
    print(len(step))
    for x,y in step:
        print(x,y)