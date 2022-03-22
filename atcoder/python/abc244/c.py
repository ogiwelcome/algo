n=int(input())
use=set()
while True:
    for i in range(1,2*n+2):
        if i not in use:
            print(i)
            use.add(i)
            break
    if len(use)==2*n+1:
        exit()
    num=int(input())
    use.add(num)