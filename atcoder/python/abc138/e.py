from collections import defaultdict
from bisect import bisect_left
s=input()
t=input()
ls,lt=len(s),len(t)
idx=defaultdict(list)
for i,ch in enumerate(s):
    idx[ch].append(i)
x=-1
for ch in t:
    arr=idx[ch]
    if len(arr)==0:
        x=-2
        break
    y=(x+1)%ls
    i=bisect_left(arr,y)
    if i<len(arr):
        nxt_x=(x+1)+arr[i]-y
    else:
        nxt_x=(x+1)+arr[0]-y+ls
    x=nxt_x
print(x+1)