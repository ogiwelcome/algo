import bisect
n=int(input())
a=[int(input()) for i in range(n)]
a=a[::-1]
LIS=[a[0]]
for i in range(1,n):
    if a[i]>=LIS[-1]:
        LIS.append(a[i])
    else:
        idx=bisect.bisect_right(LIS,a[i])
        LIS[idx]=a[i]
print(len(LIS))