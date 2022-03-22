s=list(input().split())
t=list(input().split())
if s[0]==t[0]:
    if s[1]==t[1]:
        print("Yes")
    else:
        print("No")
else:
    if s[1]==t[1]:
        print("No")
    else:
        if s[2]!=t[2]:
            print("Yes")
        else:
            print("No")