n = int(input())
a = list(map(int,input().split()))
b = [0]*n
s = 0
for i in range(n):
    if i%2==0:
        s+=a[i]
    else:
        s-=a[i]
b[0]=s
for i in range(1,n):
    b[i]=2*a[i-1]-b[i-1]
print(*b)