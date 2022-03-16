from collections import deque
n=int(input())
s=list(input())
dq=deque()
dq.append(n)
for i in range(n)[::-1]:
    if s[i]=="R":
        dq.appendleft(i)
    else:
        dq.append(i)
print(*dq)