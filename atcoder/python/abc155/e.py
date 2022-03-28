n=input()
l=len(n)
just,over=0,1
for c in n:
    c=int(c)
    just,over=min(just+c,over+(10-c)),min(just+c+1,over+(9-c))
print(just)