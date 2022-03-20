n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True)
done=[False]*(1<<n)
b=[s[0]]
done[0]=True
for d in range(n):
    j=0
    for i in range(1<<d):
        while j<(1<<n) and (done[j] or b[i]<=s[j]):
            j+=1
        if j==(1<<n):
            print("No")
            exit()
        b.append(s[j])
        done[j]=True
    b.sort(reverse=True)
print("Yes")