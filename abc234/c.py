k=int(input())
x=str(bin(k))[2:]
x=list(x)
for i in range(len(x)):
    if x[i]=="1":
        x[i]="2"
print("".join(x))