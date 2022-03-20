import math
a,b,x=map(int,input().split())
lim=a*a*b/2
if x<=lim:
    rad=math.atan(a*b*b/(2*x))
    ans=math.degrees(rad)
    print(ans)
else:
    rad=math.atan(2*(a*a*b-x)/(a**3))
    ans=math.degrees(rad)
    print(ans)