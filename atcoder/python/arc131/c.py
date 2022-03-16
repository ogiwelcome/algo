n=int(input())
a=list(map(int,input().split()))
if n%2:
    print("Win")
    exit()
x=0
for aa in a:
    x^=aa
for i in range(n):
    y=x^a[i]
    if y==0:
        print("Win")
        exit()
print("Lose")