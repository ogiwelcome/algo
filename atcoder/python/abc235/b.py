n=int(input())
h=list(map(int,input().split()))
i=0
while i+1<n and h[i]<h[i+1]:
    i+=1
print(h[i])